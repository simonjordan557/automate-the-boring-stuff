#! /usr/bin/python3

# phoneAndEmail.py: A program to extract phone numbers and email addresses from the clipboard using regex.

import re, pyperclip

inputText = pyperclip.paste()
outputString = ''

phonePattern = re.compile(r'(\+)?(44|0)(\d{4})(\s|-)?(\d{3})(\s|-)?(\d{3})')
phoneMo = phonePattern.findall(inputText)

if len(phoneMo) == 0:
    outputString += 'NO PHONE NUMBERS FOUND.\n'
else:
    outputString += 'PHONE NUMBERS FOUND:\n\n'
    for match in phoneMo:
        for i in range(len(match)):
            outputString += match[i]
        outputString += '\n'

emailPattern = re.compile(r'([a-zA-Z0-9_.%-+]+)(@)([a-zA-Z]+)(\.)([a-zA-Z.]{2,5})')
emailMo = emailPattern.findall(inputText)

if len(emailMo) == 0:
    outputString += 'NO EMAIL ADDRESSES FOUND.\n'
else:
    outputString += 'EMAIL ADDRESSES FOUND:\n\n'
    for match in emailMo:
        for i in range(len(match)):
            outputString += match[i]
        outputString += '\n'
    

pyperclip.copy(outputString)

        




