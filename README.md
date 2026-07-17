# GTBike V Awesome List
A list of mods and some tutorials to enhance your GTBike V experience.

> GTBike V is a mod for GTA V by Nestor Matas, (AKA Makinolo). **This collection is not affiliated with Makinolo or Rockstar**.

## Table of contents

- [Install GTBike V](#install-gtbike-v)
  - [Step 0 — Choose your starting point](#step-0--choose-your-starting-point)
  - [Step 1 — Find the GTA V folder](#step-1--find-the-gta-v-folder)
  - [Step 2 — Downgrade GTA V Legacy](#step-2--downgrade-gta-v-legacy-to-the-compatible-executable)
  - [Step 3 — Reduce automatic updates](#step-3--reduce-automatic-updates)
  - [Step 4 — Apply the compatible depot](#step-4--download-and-apply-the-compatible-depot)
  - [Step 5 — Confirm there are no old mods](#step-5--confirm-there-are-no-old-mods)
  - [Step 6 — Install the Windows prerequisites](#step-6--install-the-windows-prerequisites)
  - [Step 7 — Disable BattlEye](#step-7--disable-battleye-for-story-mode)
  - [Step 8 — Install GTBikeV](#step-8--install-gtbikev-and-its-scripthook-components)
  - [Step 9 — Launch GTBikeV](#step-9--launch-gtbikev)
- [Stream GTBikeV with Moonlight and VirtualHere](#stream-gtbikev-with-moonlight-and-virtualhere)
- [Important Keys](#important-keys)
- [Troubleshooting](#troubleshooting)
- [Known Issues](#known-issues)
  - [Strava Upload Helper](#strava-upload-helper)
- [Compatibility and Known Conflicts](#compatibility-and-known-conflicts)
- [Recommended Extra Mods](#recommended-extra-mods)
  - [Script and gameplay extras](#script-and-gameplay-extras)
    - [100% Game Save](#100-game-save-by-direzephyr)
    - [Straight To Story Mode](#straight-to-story-mode-by-chiheb-bacha)
    - [Activity Ghosts](#activity-ghosts-by-oldnapalm)
    - [Dynamic Population Density](#dynamic-population-density)
  - [OpenIV and visual mods](#openiv-and-visual-mods)
    - [Prepare OpenIV for cosmetic mods](#prepare-openiv-for-cosmetic-mods)
    - [VisualV](#visualv)
    - [Real Road Bike Pack](#real-road-bike-pack)
    - [Tour de France Pack](#tour-de-france-pack-by-gta-belgium)

## Install GTBike V

> This guide starts with a Windows PC that has **only Steam installed**. 

> **Do not use these mods in GTA Online.** ScriptHook and ASI mods are for single-player Story Mode only.

### Step 0 — Choose your starting point

#### GTA V is not installed

1. Open Steam and sign in.
2. Open the **Store** and search for [Grand Theft Auto V Enhanced](https://store.steampowered.com/app/3240220/Grand_Theft_Auto_V_Legacy/).
3. If you do not own GTA V, click **Add to Cart** and complete the purchase. Although the shop product is called Enhanced, the purchase includes both **Grand Theft Auto V Enhanced** and **Grand Theft Auto V Legacy**.
4. Open **Library** and select **Grand Theft Auto V Legacy**. Legacy is a separate library entry and is the recommended edition for GTBikeV.
5. If Legacy does not appear immediately, restart Steam, search the library again, and make sure hidden games are visible.
6. Click **Install**, select an installation drive, and wait for the Legacy download to finish.
7. Click **Play** once to allow Steam to install Rockstar Games Launcher and the other first-run components.
8. Sign in to or create a Rockstar Games account when prompted, and link it to Steam if requested.
9. Once Rockstar Games Launcher setup finishes, close GTA V and the launcher.
10. Continue to Step 1.

#### GTA V is already installed

1. Open Steam and select **Library**.
2. Search for `Grand Theft Auto V`.
3. If **Grand Theft Auto V Legacy** is already installed, select it and continue to Step 1.
4. If only **Grand Theft Auto V Enhanced** is installed, find the separate **Grand Theft Auto V Legacy** entry and click **Install**. Owning the current Steam package includes both editions.
5. If Legacy is owned but does not appear, restart Steam, check hidden games, and search the library again.
6. Wait for the Legacy installation to finish, then continue to Step 1.

### Step 1 — Find the GTA V folder

1. Open Steam Library.
2. Right-click **Grand Theft Auto V Legacy**.
3. Select **Manage → Browse local files**.
4. Keep the folder containing `GTA5.exe` open. This is the **game root**.

The tested location was:

```text
C:\SteamLibrary\steamapps\common\Grand Theft Auto V
```

### Step 2 — Downgrade GTA V Legacy to the compatible executable

The working setup used GTA V Legacy executable version `1.0.3889.0`. Steam's current download may install a newer executable, so download the compatible executable depot before adding the mods.

### Step 3 — Reduce automatic updates

1. In Steam Library, right-click **Grand Theft Auto V Legacy** and select **Properties**.
2. Select **Updates**.
3. Under **Automatic Updates**, choose **Wait until I launch the game**.
4. Scroll to the bottom of the Updates page and find **Build ID**.
5. If the Build ID is `24129523`, the currently installed Steam build needs the downgrade below for this setup.
6. Close the Properties window.

> This does **not** permanently lock the game version: Steam may still require an update when you launch the game.

> Keep the downloaded depot folder so you can copy the compatible files back after any update.

> Do not use **Verify Integrity of Game Files** unless troubleshooting, because verification restores Steam's current files.

> **Build ID note:** Manually copying the older depot files does not change the Build ID displayed by Steam. Steam may continue to show `24129523` afterward even though `GTA5.exe` has been replaced with the compatible `1.0.3889.0` executable.

### Step 4 — Download and apply the compatible depot

1. Close GTA V and Rockstar Games Launcher.
2. Press **Windows key + R**.
3. Enter the following and press Enter:

   ```text
   steam://open/console
   ```

4. Steam will open a **Console** tab.
5. Paste this exact command into the Steam Console and press Enter:

   ```text
   download_depot 271590 271591 6768057890420400504
   ```

   - `271590` is the GTA V Legacy app ID.
   - `271591` is the Legacy executable depot.
   - `6768057890420400504` is the manifest used by the working `1.0.3889.0` setup.

6. Wait until Steam reports that the depot download is complete. It may look inactive while downloading; do not close Steam.
7. Steam normally places the files here:

   ```text
   C:\Program Files (x86)\Steam\steamapps\content\app_271590\depot_271591
   ```

   If Steam is installed elsewhere, use the equivalent `steamapps\content\app_271590\depot_271591` folder inside the Steam installation.

8. Open the downloaded `depot_271591` folder.
9. Select all files and folders inside it and copy them into the GTA V Legacy game root from Step 1.
10. When Windows asks, choose **Replace the files in the destination**.
11. Keep the downloaded depot folder as a backup. A future Steam update or **Verify Integrity of Game Files** can restore the newest executable, in which case repeat Steps 8–10.

> This downloads and replaces the Legacy executable depot only; it is not a full second copy of GTA V.

### Step 5 — Confirm there are no old mods

Check the game root and make sure none are present:

   ```text
   NativeTrainer.asi
   OpenIV.asi
   xinput1_4.dll
   Scripts\NativeUI.dll
   mods\
   ```

If you find any, move them to a backup folder outside GTA V. Do not delete them.

### Step 6 — Install the Windows prerequisites

1. Download and install [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48).
2. Restart Windows if the installer requests it.
3. Download the latest supported **x64** [Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist).
4. Run its installer and choose **Install**. If it is already present, choose **Repair** or close the installer.
5. Restart Windows if requested.

### Step 7 — Disable BattlEye for Story Mode

1. Open Notepad.
2. Enter this exact line:

   ```text
   -nobattleye -noBE
   ```

3. Save it as `args.txt` in the game root.
4. Open **Rockstar Games Launcher** and sign in.
5. Select **Settings** in the top-right corner.
6. On the launcher Settings page, locate the BattlEye option. Depending on the launcher version, it may appear in **General** or as a checkbox labelled **Enable BattlEye**.
7. Clear the **Enable BattlEye** checkbox so it is unchecked.
8. Close the Settings page. The launcher saves the change automatically.

> The Rockstar setting and `args.txt` serve the same purpose, but using both makes the Story Mode configuration explicit when launching the Steam edition through Rockstar Games Launcher.

> If the checkbox is not shown, leave `args.txt` in the game root and continue. Do not delete the `BattlEye` folder, uninstall its service, or disable security software.

> With BattlEye disabled GTA Online will not connect. To use GTA Online later, first remove or isolate the mod files, remove the `-nobattleye -noBE` arguments, and re-enable **Enable BattlEye** in Rockstar Games Launcher.

### Step 8 — Install GTBikeV and its ScriptHook components

1. Download the **GTBikeV v0.8.0.4 Installer** from the [official downloads page](https://www.gtbikev.com/downloads/).
2. Close GTA V, Steam, and Rockstar Games Launcher.
3. Run the installer.
4. On the component-selection screen, keep **GTBikeV** selected.
5. Also select the combined option that installs **ScriptHookV and ScriptHookVDotNet**. The installer will install both required scripting components.
6. Leave GTBikeV's own files and required libraries selected.
7. When asked for the GTA V location, select the Legacy game root containing `GTA5.exe`.
8. Continue through the installer and allow it to download and install the selected components.
9. Finish and close the installer.

## Step 9 — Launch GTBikeV

1. Start GTA V with BattlEye disabled.
2. Enter Story Mode only.
3. Wait for the scripts to load.
4. Use the GTBikeV interface to select your trainer or sensors.

## Stream GTBikeV with Moonlight and VirtualHere

This optional setup lets the gaming PC run GTA V in one room while you ride beside a second computer or compatible streaming device. [Moonlight](https://moonlight-stream.org/) carries the picture, sound, keyboard, controller, and mouse input. [VirtualHere](https://www.virtualhere.com/) carries a USB ANT+ dongle or USB Bluetooth adapter over the network so it appears to be plugged into the gaming PC.

This guide assumes both devices are on the same trusted home network:

- **Gaming PC:** The Windows computer on which Steam, GTA V Legacy, and GTBikeV are installed.
- **Bike-side device:** The computer or compatible device beside the trainer. The USB sensor dongle is connected here and Moonlight displays the game here.

> Moonlight and VirtualHere use opposite client/server directions. Sunshine is the streaming **host** on the gaming PC, but the VirtualHere **Server** runs on the bike-side device because that is where the physical USB dongle is connected.

### Set up Moonlight

1. On the gaming PC, download and install [Sunshine](https://github.com/LizardByte/Sunshine/releases/latest), the recommended host for Moonlight.
2. Open Sunshine's web interface, create its administrator credentials, and finish the Windows setup. Restart the gaming PC if the installer requests it.
3. On the bike-side device, install the appropriate [Moonlight client](https://moonlight-stream.org/).
4. Connect both devices to the same network and open Moonlight. Select the gaming PC when it appears.
5. Moonlight will display a pairing PIN. Enter that PIN in Sunshine on the gaming PC and approve the device.
6. Use Sunshine's built-in **Desktop** or **Steam** entry. The Desktop entry is convenient for opening Steam, Rockstar Games Launcher, VirtualHere, and any error messages during setup.
7. In Moonlight's settings, choose a resolution and frame rate that the bike-side display and network can sustain. A wired Ethernet connection for the gaming PC—and preferably both devices—will provide the most consistent latency.

For additional platforms, controller options, or streaming outside the home, follow the official [Moonlight setup guide](https://github.com/moonlight-stream/moonlight-docs/wiki/Setup-Guide). Do not expose Sunshine or VirtualHere directly to the public internet without following their secure remote-access guidance.

### Forward the trainer dongle with VirtualHere

1. Connect the ANT+ USB dongle to the bike-side device. A USB extension cable can position an ANT+ dongle closer to the trainer and reduce wireless dropouts.
2. Install the appropriate [VirtualHere USB Server](https://www.virtualhere.com/usb_server_software) on the **bike-side device** and start it.
3. Download and run the [VirtualHere USB Client](https://www.virtualhere.com/usb_client_software) on the **gaming PC**.
4. The gaming PC's VirtualHere Client should discover the bike-side server and list its USB devices automatically.
5. Find the ANT+ dongle, right-click it, and select **Use this device**. Windows on the gaming PC will then treat it as a locally connected USB device.
6. Leave the VirtualHere Server and Client running while using GTBikeV.

The VirtualHere trial permits one shared USB device at a time, which is normally enough for one ANT+ dongle. A licence is required if you need to share multiple USB devices simultaneously.

For Bluetooth equipment, VirtualHere cannot forward Bluetooth that is built into the bike-side computer. You would need to connect and share an entire **USB Bluetooth adapter** instead. Do not share individual Bluetooth devices, and avoid having both a local and forwarded Bluetooth adapter active on the gaming PC. ANT+ is generally the simpler option for this arrangement.

### Start a streamed ride

1. Start the VirtualHere Server on the bike-side device.
2. On the gaming PC, open the VirtualHere Client and select **Use this device** for the ANT+ dongle.
3. Start Sunshine on the gaming PC if it is not already running.
4. Open Moonlight on the bike-side device and connect to **Desktop** or **Steam**.
5. Launch GTA V Legacy through Steam and enter Story Mode.
6. Press **F5**, activate GTBikeV, and select the trainer or sensors.

Only one computer can use a forwarded USB device at a time. Before unplugging the dongle or closing VirtualHere, right-click the device in the VirtualHere Client on the gaming PC and select **Stop using this device**. If GTBikeV cannot see the trainer, make sure another cycling application is not already connected to it and confirm the dongle still shows as in use by the gaming PC.

## Important Keys

| Key | Function | When it works |
| --- | --- | --- |
| **F5** | Opens or closes the **GTBikeV menu**. | In Story Mode after GTBikeV has loaded. Use this menu to activate the mod, choose a course, configure devices, and end or save a ride. |
| **F11** | Opens or closes the **GTBikeV debug window**. | After GTBikeV has loaded. Use it to check whether trainers and sensors have connected. |
| **T** | Opens the **GTBikeV multiplayer chat** so you can type a message. | After the mod has been activated and connected to GTBikeV multiplayer. Press **Enter** to send the message. |
| **Z** | Shows the list of connected GTBikeV multiplayer riders. | While connected to GTBikeV multiplayer. |
| **F8** | Opens the **Activity Ghosts menu**. | Only after installing the optional [Activity Ghosts](#activity-ghosts-by-oldnapalm) mod. |
| **F4** | Opens or closes the **ScriptHookVDotNet console**. | When ScriptHookVDotNet is running. This is a developer/debugging console, **not** the GTBikeV menu. |
| **S** | Applies the bicycle brakes. | During a GTBikeV ride. |
| **Numpad 1** | Toggles automatic steering. | During a ride; useful when following a course. |
| **Numpad 2** | Selects another random destination. | During free-roam riding. |
| **Numpad 3** | Hides or shows the ride HUD. | During a ride. |
| **Numpad 5** | Toggles ERG mode during a workout. | During a structured workout with a compatible trainer. |
| **Numpad 0** | Takes a manual screenshot. | During a ride. The screenshot is stored with the activity files. |

> **Keyboard note:** `Numpad` means the separate numeric keypad, not the number row above the letters. Laptop users may need to enable Num Lock, use an embedded keypad shortcut, or remap these controls in `GTBikeVConfig.ini`.

## Troubleshooting

### No `asiloader.log`

1. Confirm `dinput8.dll` is next to the game executable.
2. Confirm BattlEye is disabled.
3. Confirm `args.txt` contains `-nobattleye -noBE`.
4. Confirm ScriptHookV supports the installed GTA V build.

### ScriptHookVDotNet does not start

1. Confirm `ScriptHookVDotNet.asi` is in the game root.
2. Confirm all SHVDN files came from one release.
3. Install or repair .NET Framework 4.8 and the Visual C++ Redistributable.

### SHVDN starts but GTBikeV does not

1. Confirm `Scripts\GTBikeV.dll` exists.
2. Confirm the complete GTBikeV `Scripts` folder was copied.
3. Confirm `Scripts\mod_textures` exists.
4. Move optional mods out again and retest.

### GTA V was updated

Steam updates and file verification can replace the downgraded executable and mod files. Repeat the depot copy in [Step 4](#Step 4 — Download and apply the compatible depot), then rerun the GTBikeV installer from [Step 8](Step 8 — Install GTBikeV and its ScriptHook components) if its files were replaced.

## Known Issues

### Strava user lookup fails

GTBikeV's automatic Strava account-linking page may fail while looking up the Strava user. If the lookup does not complete or reports that the user cannot be found, use GTBikeV's FIT-file export and upload the activity manually instead.

#### Save the activity in GTBikeV

1. At the end of the ride, stop pedalling and wait until the activity computer shows zero speed.
2. Press **F5** to open the GTBikeV menu.
3. Select **End and save current activity**. Do not choose the option that discards the activity.
4. GTBikeV will create a `.fit` file in:

   ```text
   Documents\Rockstar Games\GTA V\Activities
   ```

   If Windows redirects Documents through OneDrive, check:

   ```text
   OneDrive\Documents\Rockstar Games\GTA V\Activities
   ```

#### Upload the FIT file manually to Strava

1. Sign in to [Strava](https://www.strava.com/).
2. Open Strava's [file upload page](https://www.strava.com/upload/select). You can also select the **+** icon, then **Upload activity → File**.
3. Select **Choose files**.
4. Open the `Activities` folder shown above and select the `.fit` file for the completed ride. Use the file's date and time to identify the correct one.
5. Wait for Strava to process the file.
6. Review the activity details, make any desired changes, and select **Save & view**.

The manual upload contains the recorded ride data; automatic Strava linking is not required. Keep the FIT file until the activity appears correctly in your Strava account, and do not upload the same file twice because that can create a duplicate activity.

### Strava Upload Helper

This repository includes an experimental Windows helper that finds the newest GTBikeV FIT file, reads its actual ride times, finds screenshots created during the same time window, and uploads them through Strava's website:

```text
tools\run_strava_uploader.ps1
```

It uses a dedicated Microsoft Edge profile and does not read or copy passwords from another browser. On the first run, sign in to Strava in the Edge window it opens. That sign-in is retained in the tool's private profile for later uploads.

#### First-time requirements

1. Install [Python 3 for Windows](https://www.python.org/downloads/windows/) if it is not already installed. Enable the Python launcher during installation.
2. Keep Microsoft Edge installed. Selenium uses Edge to operate Strava's signed-in website. The helper detects the installed Edge version and downloads the matching official Microsoft Edge WebDriver automatically on first use and after Edge updates.
3. Right-click the Windows Start button and open **Terminal** or **PowerShell**.
4. Change to the cloned collection folder, then run:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\tools\run_strava_uploader.ps1 --dry-run
   ```

   The first run creates a private Python environment under `tools\.venv` and installs the packages listed in `tools\requirements.txt`. `--dry-run` only prints the FIT file, ride times, and matching screenshots; it does not open Strava.

#### Upload the latest ride

1. End and save the activity from GTBikeV.
2. Close GTA V or wait until it has finished writing the FIT file and screenshots.
3. From the collection folder, run:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\tools\run_strava_uploader.ps1
   ```

4. If Edge asks you to sign in to Strava, complete the sign-in in that window. The helper will continue when Strava reaches its upload page.
5. Review the resulting activity and photos in Strava. If Strava has changed its web-page controls, the helper leaves Edge open and tells you to complete the remaining photo or save step manually.

Useful options:

| Option | Purpose |
| --- | --- |
| `--dry-run` | Shows which FIT file and screenshots would be used without uploading anything. |
| `--fit "C:\path\ride.fit"` | Uploads a particular FIT file instead of the newest one. |
| `--no-photos` | Uploads the FIT activity without screenshots. |
| `--force` | Allows another upload of a file already recorded by the helper. This can create a duplicate Strava activity. |
| `--activities-dir "C:\path"` | Uses a non-standard GTBikeV Activities folder. |

#### Test with synthetic rides

The `tools\test-data` folder contains two small synthetic cycling activities and one matching placeholder screenshot for each ride:

```text
test-short-ride.fit
test-short-ride-screenshot.png
test-second-ride.fit
test-second-ride-screenshot.png
```

First confirm the helper selects the correct screenshot without uploading:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\run_strava_uploader.ps1 --activities-dir .\tools\test-data --fit .\tools\test-data\test-short-ride.fit --dry-run
```

Remove `--dry-run` to perform a real Strava upload:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\run_strava_uploader.ps1 --activities-dir .\tools\test-data --fit .\tools\test-data\test-short-ride.fit
```

> **Test-data warning:** These are fake rides near central London. A real upload creates a synthetic activity in your Strava account; delete it from Strava after finishing the test.

The committed fixtures retain the timestamps from when they were generated. To create fresh test rides with current timestamps, run:

```powershell
.\tools\.venv\Scripts\python.exe .\tools\generate_test_fit_files.py
```

The generator recreates both FIT files and sets each placeholder screenshot's modified time inside its corresponding ride window.

The helper records a SHA-256 fingerprint as soon as each FIT file is submitted in `%LOCALAPPDATA%\GTBikeVStravaUploader\uploaded.json` to reduce accidental duplicates—even if the final photo or save step needs manual completion. Its persistent Edge sign-in is stored under the same local application-data folder. Do not share that folder because it contains the browser session. Strava can change its website at any time, so use `--dry-run` first after a long gap and check the selected screenshots before allowing an upload to finish.

## Compatibility and Known Conflicts

GTBikeV is a GTA V Legacy **Story Mode** script. It depends on ScriptHookV, ScriptHookVDotNet, and native Bluetooth/ANT+ libraries that communicate with cycling hardware.

| Mod, platform, or configuration | Compatibility | Explanation |
| --- | --- | --- |
| **FiveM** | **Not compatible** | GTBikeV's author has confirmed that a FiveM port would require a full rewrite. FiveM does not allow the unmanaged Bluetooth and ANT+ code used by GTBikeV to communicate with cycling hardware. Installing GTBikeV files into FiveM will not make it work. |
| **Official GTA Online** | **Not supported** | ScriptHook mods are intended for Story Mode, and this guide disables BattlEye. Do not enter GTA Online with the modded installation. GTBikeV's own multiplayer feature works independently of GTA Online. |
| **Other multiplayer clients**, such as alt:V or RAGE Multiplayer | **Not documented or supported** | This collection only covers normal GTA V Legacy Story Mode. Do not assume that support for GTA V scripts means GTBikeV's native hardware libraries will work in another multiplayer client. |
| **A second ASI loader, ScriptHookV, or ScriptHookVDotNet installation** | **Likely conflict** | The GTBikeV installer supplies the required scripting components. Another mod installer may replace `dinput8.dll`, `ScriptHookV.dll`, or the ScriptHookVDotNet files with a different version and stop GTBikeV from loading. |
| **Duplicate dependency DLLs** | **Likely conflict** | Avoid adding separate versions of libraries already supplied in `Scripts`, including UI, FIT, JSON, Bluetooth, ANT+, and networking DLLs. Keep the versions installed with GTBikeV unless another mod explicitly documents compatibility. |
| **Bike handling, player-control, autopilot, or input-overhaul mods** | **May conflict** | GTBikeV controls the bicycle, rider input, speed, resistance, and automatic course following. Another script that controls the same systems may override GTBikeV or produce unpredictable steering and movement. |
| **Mods using the same hotkeys** | **Usually compatible after rebinding** | If two menus open from the same key, change one mod's INI setting. For example, Activity Ghosts uses F8 by default and ScriptHookVDotNet uses F4 for its console. |
| **Cosmetic OpenIV mods** | **Generally compatible** | Clothing and texture replacements, such as the Tour de France Pack below, do not normally compete with GTBikeV's cycling logic. Use OpenIV's `mods` folder and keep backups. |

FiveM is the only third-party multiplayer client specifically confirmed as incompatible by the [GTBikeV author on the mod page](https://www.gta5-mods.com/scripts/gt-bike-v). The other entries marked **likely conflict** or **may conflict** are categories to treat cautiously, not claims that every mod in that category will fail.

When adding anything not listed here, install one mod at a time. If GTBikeV stops loading, remove the newest mod and restore the files installed by the official GTBikeV installer.


## Recommended Extra Mods

Install these only after the main GTBikeV setup is complete. Close GTA V and Rockstar Games Launcher before copying or replacing files. Each mod is independent, so you can install only the ones you want.

### Script and gameplay extras

These additions use save files, ASI plugins, or ScriptHookVDotNet scripts. They do not require OpenIV.

#### [100% Game Save by DireZephyr](https://www.gta5-mods.com/misc/100-save-game)
**Purpose**: Unlocks all the outfit choices for all characters.

> **Warning:** A downloaded save can replace one of your Story Mode save slots. Back up your entire profile folder before copying it.

1. Launch Story Mode at least once so GTA V creates your profile folder, then close the game.
2. Open File Explorer.
3. Go to:

   ```text
   Documents\Rockstar Games\GTA V\Profiles
   ```

   If Windows redirects Documents through OneDrive, use:

   ```text
   OneDrive\Documents\Rockstar Games\GTA V\Profiles
   ```

4. Open the folder with a random-looking profile ID, for example `A1B2C3D4`.
5. Copy that entire profile folder to a safe backup location.
6. Open the downloaded 100% save archive.
7. Copy these two files into your profile-ID folder:

   ```text
   SGTA50015
   SGTA50015.bak
   ```

8. If files with those names already exist, either keep your backup and replace them or rename the downloaded pair to an unused matching save-slot number. Both filenames must use the same number.
9. Launch GTA V and enter Story Mode.
10. If the save does not load automatically, open the pause menu and select **Game → Load Game**, then choose the new save slot.

#### [Straight To Story Mode by Chiheb-Bacha](https://www.gta5-mods.com/scripts/straight-to-story-mode)
**Purpose**: Makes getting into the game quicker.

This ASI plugin skips the legal and splash screens and takes GTA V Legacy directly to Story Mode. The GTBikeV installer has already supplied the required ScriptHookV and ASI loader.

1. Download the latest version from the linked GTA5-Mods page. Use version `1.1` or later because it supports older GTA V Legacy builds.
2. Open the downloaded archive.
3. Copy `StraightToStoryMode.asi` into the GTA V game root beside `GTA5.exe` and `dinput8.dll`.
4. Launch GTA V normally through Steam. The ASI loader will load the plugin automatically.

The final location should be:

```text
Grand Theft Auto V\StraightToStoryMode.asi
```

To remove the mod, close GTA V and delete `StraightToStoryMode.asi`. If it does not load, confirm `dinput8.dll` is still in the game root and check `StraightToStoryMode.log` and `asiloader.log` for errors.

#### [Activity Ghosts by oldnapalm](https://github.com/oldnapalm/ActivityGhosts)
**Purpose**: Gives you a physical manifestation of your previous best time to chase to push you for a PB.

1. Open the [latest Activity Ghosts release](https://github.com/oldnapalm/ActivityGhosts/releases/latest) and download its release archive.
2. Open the archive and copy these three files into the existing `Scripts` folder in the GTA V game root:

   ```text
   ActivityGhosts.dll
   ActivityGhosts.ini
   LiteDB.dll
   ```

3. Open `Scripts\ActivityGhosts.ini` if you want to change its preferences:
   - `MenuKey` opens the Activity Ghosts menu. The default is F8.
   - `LoadKey` loads or regroups the ghosts.
   - `InitialGPSPointLat` and `InitialGPSPointLong` set the starting GPS point used by FIT files.
   - `Opacity` controls ghost visibility from 1 to 5.
   - `ShowDate` controls whether each activity date appears above its ghost.
4. Save the INI after making any changes.
5. Select a course in GTBikeV and begin an activity.
6. Press **F8** to open the Activity Ghosts menu.

Activity Ghosts reads previous rides from:

```text
Documents\Rockstar Games\GTA V\Activities
```

If Documents is redirected through OneDrive, check:

```text
OneDrive\Documents\Rockstar Games\GTA V\Activities
```

The normal GTBikeV installation already supplies its other requirements. To remove Activity Ghosts, close GTA V and delete `ActivityGhosts.dll`, `ActivityGhosts.ini`, and `LiteDB.dll` from `Scripts`.

#### [Dynamic Population Density](https://www.gta5-mods.com/scripts/dynamic-population-density)

**Purpose**: Changes pedestrian and traffic density automatically according to the in-game time of day.

The mod supports GTA V Legacy and is expected to work alongside GTBikeV. However, denser traffic and crowds can reduce performance and make cycling or autopilot routes more hazardous, so begin with its default settings and lower the values if necessary.

1. Download and open the Dynamic Population Density archive.
2. Copy these two files into the GTA V game root beside `GTA5.exe`:

   ```text
   Dynamic Population Density.asi
   Dynamic Population Density.ini
   ```

3. Open `Dynamic Population Density.ini` in a text editor to adjust the traffic and pedestrian values for each time period, or leave its defaults unchanged.
4. Save the INI. The ASI loader installed with GTBikeV will load the mod automatically when Story Mode starts.

To remove the mod, close GTA V and delete both files from the game root. Avoid adding separate traffic-density or game-configuration mods at the same time unless you know they are compatible, because their changes can overlap and make the downgraded Legacy setup less stable.

### OpenIV and visual mods

The following cosmetic mods all use OpenIV. Prepare OpenIV once, then install any of the related visual, bicycle-texture, or clothing mods listed immediately afterward.

#### Prepare OpenIV for cosmetic mods

VisualV, Real Road Bike Pack, and Tour de France Pack use [OpenIV](https://openiv.com/) to place replacement files safely in a separate `mods` folder. Complete this setup once before installing any of those three mods:

1. Download and install OpenIV.
2. Start OpenIV, choose **Grand Theft Auto V → Windows**, and select the GTA V Legacy folder if it is not detected automatically.
3. Open **Tools → ASI Manager**.
4. Install **OpenIV.asi**. If ASI Loader is already shown as installed, leave it as it is because the GTBikeV installer supplied `dinput8.dll`.
5. Enable **Edit mode**.
6. Allow OpenIV to create the `mods` folder when prompted. Always modify the copies inside `mods`, not the original game archives.

#### [VisualV](https://www.gta5-mods.com/misc/visualv)

**Purpose**: Improves GTA V's weather, lighting, colours, fog, shadows, and other visual effects.

VisualV is expected to work with GTBikeV because it changes graphics rather than cycling controls or scripts. Download the **Legacy** release, not the Enhanced release. Start with the base VisualV package; its optional ReShade and ENB presets add more rendering changes and are not required.

1. Complete [Prepare OpenIV for cosmetic mods](#prepare-openiv-for-cosmetic-mods) above.
2. Download the GTA V **Legacy** version of VisualV from the linked page and open the archive.
3. In OpenIV, select **Tools → Package Installer**.
4. Select `VisualV.oiv` from the downloaded archive.
5. Choose **Install to "mods" folder** and complete the installation.
6. Close OpenIV.

Avoid combining VisualV's optional advanced motion-blur script with NaturalVision Evolved or NaturalVision Remastered scripts. To remove VisualV, use the uninstaller included with its download if available, or restore the affected archive copies in OpenIV's `mods` folder without deleting unrelated mods.

#### [Real Road Bike Pack](https://www.gta5-mods.com/paintjobs/real-road-bike-pack)

**Purpose**: Replaces the textures of GTA V's three standard road/triathlon bikes with real-world-style designs.

This pack is expected to work with GTBikeV because it only replaces textures on the standard `tribike`, `tribike2`, and `tribike3` models. Do not combine it with another texture pack that replaces the same files: the last files installed will overwrite the earlier ones.

1. Complete [Prepare OpenIV for cosmetic mods](#prepare-openiv-for-cosmetic-mods) above.
2. Download and open the Real Road Bike Pack archive.
3. In OpenIV, navigate to:

   ```text
   mods\x64e.rpf\levels\gta5\vehicles.rpf
   ```

4. If `x64e.rpf` is not yet in `mods`, let OpenIV copy it there before making changes.
5. Back up the existing versions of these six files:

   ```text
   tribike.ytd
   tribike+hi.ytd
   tribike2.ytd
   tribike2+hi.ytd
   tribike3.ytd
   tribike3+hi.ytd
   ```

6. With **Edit mode** enabled, replace those files with the matching files from the downloaded pack.
7. Close OpenIV.

To remove the pack, restore the six backed-up files at the same path. Do not remove the whole modified `x64e.rpf` if another mod also uses it.

#### [Tour de France Pack by GTA Belgium](https://www.gta5-mods.com/player/tour-de-france-pack)
**Purpose**: Gives you Tour de France outfits.

> **OpenIV modification:** This pack replaces game clothing files. Back up the affected files and use OpenIV's `mods` folder rather than editing the original archives. Keep this optional modification out of the initial GTBikeV installation.

The pack contains yellow Tour de France outfits for Franklin and Michael. These replace their existing Triathlon outfits. It also contains an optional paintjob for a separate Audi RS4 mod; the car is not required for the cycling outfits.

##### Install the outfits

1. Complete [Prepare OpenIV for cosmetic mods](#prepare-openiv-for-cosmetic-mods) above.
2. Download and open the Tour de France Pack archive.
3. Open its `files` folder. It contains separate `Franklin`, `Michael`, and Audi folders, so you can choose which parts to install.
4. Open the text file supplied inside the `Franklin` folder and navigate to that exact archive path in OpenIV.
5. Use OpenIV to replace the listed Triathlon outfit files with the matching Franklin files from the pack.
6. Repeat the process using the path text file and replacement files in the `Michael` folder.
7. Close OpenIV after all replacements finish.

The Tour de France clothing will appear when Franklin or Michael equips the Triathlon outfit that the pack replaced.

##### Optional Audi paintjob

1. First install Dreamsky's [2013 Audi RS4 Avant](https://www.gta5-mods.com/vehicles/2013-audi-rs4-avant) by following that mod's instructions.
2. In OpenIV, open the installed car's `stratum.ytd` and `stratum+hi.ytd` texture dictionaries.
3. Replace the relevant image texture with the Tour de France texture from the pack's Audi folder.
4. Save the modified texture dictionaries in the `mods` folder.

To remove the outfits or paintjob, restore the backed-up files in the same OpenIV paths or remove their modified archive copies from the `mods` folder. Do not delete unrelated files from `mods`.


