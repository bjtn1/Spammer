"""
@author Brandon Jose Tenorio Noguera
"""
# !/usr/bin/env python3

import argparse
import os
import time

import pyautogui


def countdown(time_in_seconds: int) -> None:
    """Displays a countdown timer

    Args:
        time_in_seconds (int): Time in seconds
    """
    while time_in_seconds:
        mins, secs = divmod(time_in_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        time_in_seconds -= 1


def main():
    # TODO Add epilog
    parser = argparse.ArgumentParser(
        prog="spam",
        description="Writes every line or word from a .txt file to cursor",
    )

    parser.add_argument("file", help="Path to a .txt file")

    parser.add_argument(
        "write",
        help="Write every line or word from .txt file",
        choices=["line", "word"],
    )

    parser.add_argument(
        "-t",
        "--time",
        help="Time in seconds to wait before typing. Default is 10 seconds",
        default=10,
        type=int,
    )

    args = parser.parse_args()

    path_to_file: str = os.path.abspath(args.file)
    wait_time_in_seconds: int = args.time
    what_to_write: str = args.write  # This is either "word" or "line"

    countdown(wait_time_in_seconds)

    # exit(0)

    with open(path_to_file, "r") as file:
        lines = file.read().splitlines()

        # Obtain every word from every line in the file
        words = [word for line in lines for word in line.split()]

    if what_to_write == "line":
        for line in lines:
            pyautogui.typewrite(f"{line}\n")
    else:
        for word in words:
            pyautogui.typewrite(f"{word}\n")


if __name__ == "__main__":
    main()
