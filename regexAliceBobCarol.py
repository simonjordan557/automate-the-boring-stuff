import re

def aliceBobCarol(text):
    aliceBobCarolRegex = re.compile(r'(alice|bob|carol)\s(eats|throws|pets)\s(cats|apples|baseballs)\.', re.I)
    mo = aliceBobCarolRegex.search(text)
    return mo

print(aliceBobCarol('Alice eats apples.').group())
print(aliceBobCarol('Bob pets cats.').group())
print(aliceBobCarol('Carol throws baseballs.').group())
print(aliceBobCarol('Alice throws Apples.').group())
print(aliceBobCarol('BOB EATS CATS.').group())

print(aliceBobCarol('RoboCop eats apples.') == None)
print(aliceBobCarol('ALICE THROWS FOOTBALLS.') == None)
print(aliceBobCarol('Carol eats 7 cats.') == None)
