import re

def nakamoto(text):
    
    nakamotoRegex = re.compile(r'([A-Z]\w*)\sNakamoto')
    mo = nakamotoRegex.search(text)
    return mo

print(nakamoto('Satoshi Nakamoto').group())
print(nakamoto('Alice Nakamoto').group())
print(nakamoto('RoboCop Nakamoto').group())

print(nakamoto('satoshi Nakamoto') == None)
print(nakamoto('Mr. Nakamoto') == None)
print(nakamoto('Nakamoto') == None)
print(nakamoto('Satoshi nakamoto') == None)

