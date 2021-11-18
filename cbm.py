#!/usr/bin/env python3

CLIPBOARD_QUEUE_FILE = "~/.clipboard"
CLIPBOARD_SEPARATOR = "\n\n\n"

import os
import argparse
import pyperclip

def update_clipboard(backward: bool):
    try:
        with open(os.path.expanduser(CLIPBOARD_QUEUE_FILE)) as cbf:
            messages = cbf.read().split(CLIPBOARD_SEPARATOR)
            messages = [m.strip() for m in messages]
            if backward:
                messages.reverse()
            it = iter(messages)
    except:
        it = iter([])

    current_message = pyperclip.paste().strip()

    while True:
        try:
            message = next(it)
            if message == current_message:
                new_message = next(it)
                break
        except StopIteration:
            new_message = None
            break

    if new_message:
        pyperclip.copy(new_message)

if __name__ == "__main__":

    note = f"A smart clipboard manager that iterate over {CLIPBOARD_QUEUE_FILE} if the current clipboard is exactly one line of it."
    parser = argparse.ArgumentParser(description=note)
    parser.add_argument(
        "-b", "--backward", help="get an item prior to the current one", action="store_true"
    )
    args = parser.parse_args()

    update_clipboard(args.backward)
