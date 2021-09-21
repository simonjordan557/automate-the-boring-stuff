import re

def regexStrip(text, target=' '):
    startPattern = re.compile(r'^(' + target + ')+')
    endPattern = re.compile(r'(' + target + ')+$')

    output = startPattern.sub('', text)
    return endPattern.sub('', output)
    
print(regexStrip('       My name is Simon         '))
print(regexStrip('xxxxxMy name is Simonxxxxx', 'x'))
