#!/usr/bin/env python3
"""Upload a GTBikeV FIT activity and its matching screenshots to Strava."""

from __future__ import annotations

import argparse
import ctypes
import hashlib
import json
import os
import sys
import time
import urllib.request
import winreg
import zipfile
from ctypes import wintypes
from datetime import datetime, timedelta, timezone
from pathlib import Path

import fitdecode
from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


UPLOAD_URL = "https://www.strava.com/upload/select"
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}


def default_activities_dir() -> Path:
    candidates = []
    one_drive = os.environ.get("OneDrive")
    if one_drive:
        candidates.append(Path(one_drive) / "Documents/Rockstar Games/GTA V/Activities")
    candidates.append(Path.home() / "Documents/Rockstar Games/GTA V/Activities")
    for candidate in candidates:
        if candidate.is_dir():
            return candidate
    return candidates[0]


def newest_fit(folder: Path) -> Path:
    files = list(folder.glob("*.fit")) + list(folder.glob("*.FIT"))
    if not files:
        raise FileNotFoundError(f"No FIT files were found in {folder}")
    return max(files, key=lambda path: path.stat().st_mtime)


def fit_time_window(path: Path) -> tuple[datetime, datetime]:
    start = None
    end = None
    with fitdecode.FitReader(path) as fit:
        for frame in fit:
            if not isinstance(frame, fitdecode.FitDataMessage):
                continue
            timestamp = frame.get_value("timestamp", fallback=None)
            if isinstance(timestamp, datetime):
                timestamp = timestamp.astimezone(timezone.utc)
                start = timestamp if start is None else min(start, timestamp)
                end = timestamp if end is None else max(end, timestamp)
            if frame.name == "session":
                session_start = frame.get_value("start_time", fallback=None)
                elapsed = frame.get_value("total_elapsed_time", fallback=None)
                if isinstance(session_start, datetime):
                    session_start = session_start.astimezone(timezone.utc)
                    start = session_start if start is None else min(start, session_start)
                    if isinstance(elapsed, (int, float)):
                        session_end = session_start + timedelta(seconds=float(elapsed))
                        end = session_end if end is None else max(end, session_end)
    if start is None or end is None:
        modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
        return modified - timedelta(hours=1), modified
    return start, end


def matching_screenshots(folder: Path, start: datetime, end: datetime) -> list[Path]:
    # GTBikeV writes screenshots during the ride. A small margin accommodates
    # delayed disk writes and screenshots taken just before/after saving.
    lower = start - timedelta(minutes=2)
    upper = end + timedelta(minutes=10)
    matches = []
    for path in folder.iterdir():
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES:
            modified = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
            if lower <= modified <= upper:
                matches.append(path.resolve())
    return sorted(matches, key=lambda path: path.stat().st_mtime)


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def state_path() -> Path:
    root = Path(os.environ.get("LOCALAPPDATA", Path.home())) / "GTBikeVStravaUploader"
    root.mkdir(parents=True, exist_ok=True)
    return root / "uploaded.json"


def load_uploaded() -> set[str]:
    path = state_path()
    if not path.exists():
        return set()
    try:
        return set(json.loads(path.read_text(encoding="utf-8")))
    except (OSError, ValueError):
        return set()


def save_uploaded(values: set[str]) -> None:
    state_path().write_text(json.dumps(sorted(values), indent=2), encoding="utf-8")


def application_data_dir() -> Path:
    root = Path(os.environ.get("LOCALAPPDATA", Path.home())) / "GTBikeVStravaUploader"
    root.mkdir(parents=True, exist_ok=True)
    return root


def installed_edge_version() -> str:
    registry_paths = (
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Edge\BLBeacon"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Edge\BLBeacon"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\WOW6432Node\Microsoft\Edge\BLBeacon"),
    )
    for hive, key_path in registry_paths:
        try:
            with winreg.OpenKey(hive, key_path) as key:
                version, _ = winreg.QueryValueEx(key, "version")
                if version:
                    return str(version)
        except OSError:
            continue
    edge_paths = (
        Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"))
        / "Microsoft/Edge/Application/msedge.exe",
        Path(os.environ.get("ProgramFiles", r"C:\Program Files"))
        / "Microsoft/Edge/Application/msedge.exe",
    )
    for edge_path in edge_paths:
        if not edge_path.is_file():
            continue
        size = ctypes.windll.version.GetFileVersionInfoSizeW(str(edge_path), None)
        if not size:
            continue
        data = ctypes.create_string_buffer(size)
        if not ctypes.windll.version.GetFileVersionInfoW(str(edge_path), 0, size, data):
            continue
        value = ctypes.c_void_p()
        value_size = wintypes.UINT()
        if not ctypes.windll.version.VerQueryValueW(
            data, "\\", ctypes.byref(value), ctypes.byref(value_size)
        ):
            continue
        words = ctypes.cast(value, ctypes.POINTER(wintypes.DWORD * 13)).contents
        version_ms, version_ls = words[2], words[3]
        return ".".join(
            str(part) for part in (
                version_ms >> 16, version_ms & 0xFFFF,
                version_ls >> 16, version_ls & 0xFFFF,
            )
        )
    raise RuntimeError("Microsoft Edge is installed, but its version could not be detected.")


def matching_edge_driver() -> Path:
    version = installed_edge_version()
    driver_dir = application_data_dir() / "Drivers" / version
    driver = driver_dir / "msedgedriver.exe"
    if driver.is_file():
        return driver

    driver_dir.mkdir(parents=True, exist_ok=True)
    archive = driver_dir / "edgedriver_win64.zip"
    url = f"https://msedgedriver.microsoft.com/{version}/edgedriver_win64.zip"
    print(f"Downloading Microsoft Edge WebDriver {version}...")
    try:
        urllib.request.urlretrieve(url, archive)
        with zipfile.ZipFile(archive) as zipped:
            zipped.extract("msedgedriver.exe", driver_dir)
    except Exception as error:
        raise RuntimeError(
            f"Could not download the matching Edge WebDriver from {url}: {error}"
        ) from error
    finally:
        if archive.exists():
            archive.unlink()
    return driver


def edge_driver() -> webdriver.Edge:
    profile = application_data_dir() / "EdgeProfile"
    profile.mkdir(parents=True, exist_ok=True)
    options = webdriver.EdgeOptions()
    options.add_argument(f"--user-data-dir={profile}")
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    service = EdgeService(executable_path=str(matching_edge_driver()))
    return webdriver.Edge(service=service, options=options)


def wait_for_strava_login(driver: webdriver.Edge) -> None:
    driver.get(UPLOAD_URL)
    if "/login" in driver.current_url:
        print("Sign in to Strava in the opened Edge window. Waiting for the upload page...")
        WebDriverWait(driver, 300).until(lambda browser: "/upload" in browser.current_url)


def fit_input(driver: webdriver.Edge):
    def locate(browser):
        for element in browser.find_elements(By.CSS_SELECTOR, "input[type='file']"):
            accept = (element.get_attribute("accept") or "").lower()
            if not accept or "fit" in accept or "tcx" in accept or "gpx" in accept:
                return element
        return False
    return WebDriverWait(driver, 60).until(locate)


def dismiss_cookie_notice(driver: webdriver.Edge) -> None:
    try:
        decline = driver.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline")
        if decline.is_displayed():
            decline.click()
    except (NoSuchElementException, ElementNotInteractableException):
        pass


def add_photos(driver: webdriver.Edge, photos: list[Path]) -> bool:
    if not photos:
        return True
    try:
        edit = WebDriverWait(driver, 30).until(
            lambda browser: next(
                (element for element in browser.find_elements(By.XPATH, "//a | //button")
                 if "edit this activity" in (element.accessible_name or "").lower()
                 and element.is_displayed()),
                False,
            )
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit)
        edit.click()
    except (TimeoutException, ElementNotInteractableException):
        return False

    deadline = time.time() + 90
    while time.time() < deadline:
        for element in driver.find_elements(By.CSS_SELECTOR, "input[type='file']"):
            accept = (element.get_attribute("accept") or "").lower()
            if ("image" in accept or ".jpg" in accept or ".png" in accept
                    or (not accept and "/edit" in driver.current_url)):
                element.send_keys("\n".join(str(path) for path in photos))
                return save_edit(driver)
        time.sleep(2)
    return False


def click_visible_button(driver: webdriver.Edge, labels: tuple[str, ...], timeout: int) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        dismiss_cookie_notice(driver)
        for label in labels:
            for button in driver.find_elements(
                By.XPATH, f"//button[contains(normalize-space(), '{label}')]"
            ):
                try:
                    if button.is_displayed() and button.is_enabled():
                        driver.execute_script(
                            "arguments[0].scrollIntoView({block: 'center'});", button
                        )
                        button.click()
                        return True
                except (
                    ElementClickInterceptedException,
                    ElementNotInteractableException,
                    StaleElementReferenceException,
                ):
                    continue
        time.sleep(2)
    return False


def save_activity(driver: webdriver.Edge) -> bool:
    return click_visible_button(
        driver, ("Save & View", "Save & view", "Save and view", "Save Activity"), 90
    )


def save_edit(driver: webdriver.Edge) -> bool:
    previous_url = driver.current_url
    if not click_visible_button(driver, ("Save",), 90):
        return False
    deadline = time.time() + 90
    while time.time() < deadline:
        if driver.current_url != previous_url and "/activities/" in driver.current_url:
            return True
        time.sleep(2)
    return "/activities/" in driver.current_url and not driver.current_url.endswith("/edit")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fit", type=Path, help="FIT file to upload; defaults to the newest FIT file")
    parser.add_argument("--activities-dir", type=Path, default=default_activities_dir())
    parser.add_argument("--no-photos", action="store_true", help="Do not attach matching screenshots")
    parser.add_argument("--dry-run", action="store_true", help="Show selected files without opening Strava")
    parser.add_argument("--force", action="store_true", help="Allow a FIT file previously recorded as uploaded")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    activities = args.activities_dir.expanduser().resolve()
    fit = (args.fit.expanduser().resolve() if args.fit else newest_fit(activities))
    if not fit.is_file():
        raise FileNotFoundError(fit)

    start, end = fit_time_window(fit)
    photos = [] if args.no_photos else matching_screenshots(activities, start, end)
    digest = file_digest(fit)
    uploaded = load_uploaded()
    if digest in uploaded and not args.force:
        print("This FIT file was already uploaded by this tool. Use --force to upload it again.")
        return 2

    print(f"FIT: {fit}")
    print(f"Ride: {start.astimezone()} to {end.astimezone()}")
    print(f"Matching screenshots ({len(photos)}):")
    for photo in photos:
        print(f"  {photo}")
    if args.dry_run:
        return 0

    driver = edge_driver()
    try:
        wait_for_strava_login(driver)
        fit_input(driver).send_keys(str(fit))
        # Treat submission as used immediately. Strava may already have accepted
        # the activity even if a later photo or Save control cannot be located.
        uploaded.add(digest)
        save_uploaded(uploaded)
        print("FIT file submitted. Waiting for Strava to process it...")
        time.sleep(5)
        saved = save_activity(driver)
        if saved:
            try:
                WebDriverWait(driver, 60).until(
                    lambda browser: "/activities/" in browser.current_url
                )
            except TimeoutException:
                saved = False
        photos_added = add_photos(driver, photos) if saved else False
        if not saved or not photos_added:
            print("Strava's page controls were not fully recognised.")
            print("The browser has been left open; attach any listed screenshots and click Save & view.")
            return 1
        print("Activity and matching screenshots uploaded to Strava.")
        return 0
    except TimeoutException:
        print("Timed out waiting for Strava. The browser has been left open for manual completion.")
        return 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, fitdecode.FitError, RuntimeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
