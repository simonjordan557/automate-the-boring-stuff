import re

upperCaseRegex = re.compile(r'[A-Z]+')
lowerCaseRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'\d+')
lengthRegex = re.compile(r'\S{8,}')

def passwordCheck(text):

    if upperCaseRegex.search(text) == None:
        return 'Password: ' + text + ' needs at least one upper case letter.'
    if lowerCaseRegex.search(text) == None:
        return 'Password: ' + text + ' needs at least one lower case letter.'
    if digitRegex.search(text) == None:
        return 'Password: ' + text + ' needs at least one digit.'
    if lengthRegex.search(text) == None:
        return 'Password: ' + text + ' needs to be at least 8 characters long.'

    return 'Password: ' + text + ' is secure!'

print(passwordCheck('JohnSmith99'))
print(passwordCheck('johnSmith99'))
print(passwordCheck('johnsmith99'))
print(passwordCheck('JOHNSMITH99'))
print(passwordCheck('johnsmith'))
print(passwordCheck('JohnSmith'))
print(passwordCheck('JSmith9'))



      

