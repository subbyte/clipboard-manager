# A Personal Clipboard Manager

### Requirements
- `pyperclip` (Python package)
- `xsel` (system package/program/utility)

### Usage
Put the sequence of messages in `~/.clipboard`. Use `cbm.py` to iterate over the messages (and update clipboard) if the current clipboard is one of them. Use `cbm.py -b` to iterate backward (and update clipboard).

By default, the messages are separated by `\n\n\n` to support multi-line message in clipboard.

You can customize `CLIPBOARD_QUEUE_FILE` and/or `CLIPBOARD_SEPARATOR` in `cbm.py`.
