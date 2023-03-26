"""
@author Brandon Jose Tenorio Noguera
"""
# !/usr/bin/env python3

import argparse
import os
import time
from threading import Thread

import pyautogui
from pynput import keyboard


def on_press(key):
    try:
        if key == keyboard.Key.shift:
            # Exit the program if the user presses 'q'
            print("Exiting...")
            return False
    except AttributeError:
        pass


def countdown(time_in_seconds: int) -> None:
    while time_in_seconds:
        mins, secs = divmod(time_in_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        time_in_seconds -= 1


def spam_every_line(lines_list: list[str], time_in_seconds: int) -> None:
    countdown(time_in_seconds)

    for line in lines_list:
        pyautogui.typewrite(f"{line}\n")


def spam_every_word(words_list: list[str], time_in_seconds: int) -> None:
    countdown(time_in_seconds)

    for word in words_list:
        pyautogui.typewrite(f"{word}\n")


def main():
    parser = argparse.ArgumentParser(
        prog="spam",
        description="A program that writes every line or word from a .txt file to wherever cursor is placed",  # noqa
    )

    parser.add_argument("file", help="Path to a .txt file")

    parser.add_argument(
        "write",
        help="Write every word or line in .txt file",
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
    what_to_write: str = args.write

    with open(path_to_file, "r") as file:
        lines = file.read().splitlines()
        words = [word for line in lines for word in line.split()]

    if what_to_write == "line":
        spam_every_line(lines, wait_time_in_seconds)

    elif what_to_write == "word":
        spam_every_word(words, wait_time_in_seconds)

    else:
        exit(
            "Unrecognized parameter. Chosose either word or line for what to type."  # noqa
        )


if __name__ == "__main__":
    main()
