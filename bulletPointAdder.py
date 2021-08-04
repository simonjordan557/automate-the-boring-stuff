#! /usr/bin/python3

# Add bullet points to the start of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines.
lines = text.split('\n')

# Loop through lines, adding a star to each.
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

# Join all lines into a single string, seperated by \n.
text = '\n'.join(lines)

# Copy edited text back to the clipboard.
pyperclip.copy(text)
