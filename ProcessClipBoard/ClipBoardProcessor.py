#! python3
# This python app can process text from Clipboard

import pyperclip


# Copy to clipboard!
pyperclip.copy('The text to be copied to the clipboard.')


# Read what's in the clipboard
print(pyperclip.paste())