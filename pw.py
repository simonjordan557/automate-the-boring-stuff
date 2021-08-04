#! /usr/bin/python3

# pw.py - An insecure password locker program.

PASSWORDS = {'email':'pa55word', 'blog':'abcdef', 'luggage':'1234'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: pythgon pw.py [account] - copy account password to clipboard')
    sys.exit()

account = sys.argv[1]    # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    
