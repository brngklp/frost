import pyperclip

def copy_to_clipboard(password: str) -> None:
    """
    Copy the password to the clipboard.
    """
    pyperclip.copy(password)
