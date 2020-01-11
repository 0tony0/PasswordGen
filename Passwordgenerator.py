import random
passwordString = ""
passwordList = []
passwordLength = int(input("How many characters do you want the password to have? "))
def numberGenerator():
    return random.randint(0, 9)
def symbolGenerator():
    symbolNumber = random.randint(33, 47)
    symbol = chr(symbolNumber)
    return symbol
def letterGenerator():
    uppercaseLowercase = random.randint(1,2)
    if (uppercaseLowercase == 2):
        letterNumber = random.randint(65, 90)
    if (uppercaseLowercase == 1):
        letterNumber = random.randint(97, 122)
    letter = chr(letterNumber)
    return letter

def lettersymbolorNumber():
    lettersNumbers = random.randint(1,3)
    if (lettersNumbers == 1):
        passwordList.append(number)
    if (lettersNumbers == 2):
        passwordList.append(letter)
    if (lettersNumbers == 3):
        passwordList.append(symbol)
while (passwordLength > 0):
    letter = letterGenerator()
    number = numberGenerator()
    symbol = symbolGenerator()
    lettersymbolorNumber()
    passwordLength = passwordLength - 1

for i in passwordList:
    passwordString += str(i)
print("The password that has generated is", passwordString)