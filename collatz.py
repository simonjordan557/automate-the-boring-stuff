def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result

def authenticateInput():
    global collatzNumber
    print('Enter a number: ')
    try:
        collatzNumber = int(input())
    except:
        print('You must enter an integer!')
        return False
    return True

validInput = False
collatzNumber = -1

while validInput == False:
    validInput = authenticateInput()
    
while collatzNumber != 1:    
    collatzNumber = collatz(collatzNumber)

    
        
