spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = [1, 2, 3, 4, 5]

def format(listToFormat):
    for i in range(len(listToFormat)):
        if i < len(listToFormat) - 1:
            print(str(listToFormat[i]) + ', ', end='')
        else:
            print('and ' + str(listToFormat[i]))

format(spam)
format(eggs)
            
