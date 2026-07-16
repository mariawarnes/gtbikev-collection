#!/usr/bin/env python3
"""Generate small synthetic FIT rides and matching screenshot fixtures."""

from __future__ import annotations

import argparse
import math
import os
import struct
import zlib
from datetime import datetime, timedelta, timezone
from pathlib import Path


FIT_EPOCH = datetime(1989, 12, 31, tzinfo=timezone.utc)
CRC_TABLE = (0x0000, 0xCC01, 0xD801, 0x1400, 0xF001, 0x3C00, 0x2800, 0xE401,
             0xA001, 0x6C00, 0x7800, 0xB401, 0x5000, 0x9C01, 0x8801, 0x4400)


def crc(data: bytes, initial: int = 0) -> int:
    value = initial
    for byte in data:
        tmp = CRC_TABLE[value & 0xF]
        value = (value >> 4) & 0x0FFF
        value ^= tmp ^ CRC_TABLE[byte & 0xF]
        tmp = CRC_TABLE[value & 0xF]
        value = (value >> 4) & 0x0FFF
        value ^= tmp ^ CRC_TABLE[(byte >> 4) & 0xF]
    return value


def fit_time(value: datetime) -> int:
    return int((value.astimezone(timezone.utc) - FIT_EPOCH).total_seconds())


def semicircles(degrees: float) -> int:
    return round(degrees * (2**31 / 180.0))


def definition(local: int, global_number: int, fields: list[tuple[int, int, int]]) -> bytes:
    result = bytearray((0x40 | local, 0, 0))
    result += struct.pack("<H", global_number)
    result.append(len(fields))
    for number, size, base_type in fields:
        result += bytes((number, size, base_type))
    return bytes(result)


def data_message(local: int, fmt: str, *values: int) -> bytes:
    return bytes((local,)) + struct.pack("<" + fmt, *values)


def build_ride(start: datetime, duration_seconds: int, distance_metres: float,
               latitude: float, longitude: float) -> bytes:
    points = max(12, duration_seconds // 15 + 1)
    elapsed_step = duration_seconds / (points - 1)
    distance_step = distance_metres / (points - 1)
    average_speed = distance_metres / duration_seconds
    end = start + timedelta(seconds=duration_seconds)
    payload = bytearray()

    file_fields = [(0, 1, 0x00), (1, 2, 0x84), (2, 2, 0x84),
                   (3, 4, 0x8C), (4, 4, 0x86), (5, 2, 0x84)]
    payload += definition(0, 0, file_fields)
    payload += data_message(0, "BHHIIH", 4, 1, 1, 0x47544256, fit_time(start), 1)

    record_fields = [(253, 4, 0x86), (0, 4, 0x85), (1, 4, 0x85),
                     (2, 2, 0x84), (3, 1, 0x02), (4, 1, 0x02),
                     (5, 4, 0x86), (6, 2, 0x84), (7, 2, 0x84)]
    payload += definition(1, 20, record_fields)
    for index in range(points):
        fraction = index / (points - 1)
        timestamp = start + timedelta(seconds=elapsed_step * index)
        # A short, gently curving route near central London.
        lat = latitude + 0.004 * fraction
        lon = longitude + 0.008 * fraction + math.sin(fraction * math.pi) * 0.001
        altitude = 35 + math.sin(fraction * math.pi) * 8
        heart_rate = round(105 + 25 * math.sin(fraction * math.pi))
        cadence = round(72 + 10 * math.sin(fraction * math.pi))
        speed = average_speed * (0.9 + 0.2 * math.sin(fraction * math.pi))
        power = round(120 + 70 * math.sin(fraction * math.pi))
        payload += data_message(
            1, "IiiHBBIHH", fit_time(timestamp), semicircles(lat), semicircles(lon),
            round((altitude + 500) * 5), heart_rate, cadence,
            round(distance_step * index * 100), round(speed * 1000), power)

    session_fields = [(253, 4, 0x86), (2, 4, 0x86), (7, 4, 0x86),
                      (8, 4, 0x86), (9, 4, 0x86), (5, 1, 0x00),
                      (6, 1, 0x00), (14, 2, 0x84), (15, 2, 0x84),
                      (16, 1, 0x02), (17, 1, 0x02), (18, 1, 0x02),
                      (19, 1, 0x02), (20, 2, 0x84), (21, 2, 0x84),
                      (25, 2, 0x84), (26, 2, 0x84), (0, 1, 0x00),
                      (1, 1, 0x00), (28, 1, 0x00)]
    payload += definition(2, 18, session_fields)
    payload += data_message(
        2, "IIIIIBBHHBBBBHHHHBBB", fit_time(end), fit_time(start),
        duration_seconds * 1000, duration_seconds * 1000, round(distance_metres * 100),
        2, 58, round(average_speed * 1000), round(average_speed * 1.15 * 1000),
        120, 132, 78, 84, 155, 195, 0, 1, 9, 1, 0)

    activity_fields = [(253, 4, 0x86), (0, 1, 0x00), (1, 1, 0x00),
                       (2, 4, 0x86), (3, 2, 0x84), (4, 1, 0x00), (5, 4, 0x86)]
    payload += definition(3, 34, activity_fields)
    payload += data_message(3, "IBBIHBI", fit_time(end), 26, 1,
                            duration_seconds * 1000, 1, 0, fit_time(end))

    header_without_crc = struct.pack("<BBHI4s", 14, 0x20, 2171, len(payload), b".FIT")
    header = header_without_crc + struct.pack("<H", crc(header_without_crc))
    body = header + payload
    return body + struct.pack("<H", crc(body))


def placeholder_png(label: str) -> bytes:
    # A valid 1x1 RGB PNG. The identifying label is stored in a tEXt chunk.
    signature = b"\x89PNG\r\n\x1a\n"
    def chunk(kind: bytes, content: bytes) -> bytes:
        return struct.pack(">I", len(content)) + kind + content + struct.pack(">I", zlib.crc32(kind + content) & 0xFFFFFFFF)
    raw = b"\x00\x44\x88\xCC"
    return (signature + chunk(b"IHDR", struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0))
            + chunk(b"tEXt", b"Description\x00" + label.encode("utf-8"))
            + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "test-data")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).replace(microsecond=0)
    rides = [
        ("test-short-ride", now - timedelta(minutes=40), 300, 1500.0, 51.5074, -0.1278),
        ("test-second-ride", now - timedelta(days=1, minutes=25), 600, 3200.0, 51.5007, -0.1246),
    ]
    for name, start, duration, distance, lat, lon in rides:
        fit_path = output / f"{name}.fit"
        image_path = output / f"{name}-screenshot.png"
        fit_path.write_bytes(build_ride(start, duration, distance, lat, lon))
        image_path.write_bytes(placeholder_png(f"Synthetic screenshot for {name}"))
        screenshot_time = (start + timedelta(seconds=duration / 2)).timestamp()
        os.utime(image_path, (screenshot_time, screenshot_time))
        print(f"Created {fit_path}")
        print(f"Created {image_path}")


if __name__ == "__main__":
    main()
