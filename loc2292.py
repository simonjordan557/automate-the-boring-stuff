spam = ['apple', 'cherry', 'banana', 'eggplant', 'date']

print(spam.index('eggplant'))

spam.append('yam')

print(spam)

spam.insert(1, 'potato')

print(spam)

spam.remove('cherry')

for i in range(len(spam)):
    print(str(i) + ':    ' + spam[i])

del(spam[4])
print()

for i in range(len(spam)):
    print(str(i) + ':    ' + spam[i])

spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
