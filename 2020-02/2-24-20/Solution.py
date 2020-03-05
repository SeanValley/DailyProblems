#main() contains tests for possibleDecrypts()
#possibleDecrypts(message) will return how many possible messages
#can be deciphered from a given string of numbers
#where 1=a, 2=b, 3=c, etc.

def main():
    totalPossible = possibleDecrypts("111")
    print(totalPossible)

    totalPossible = possibleDecrypts("123")
    print(totalPossible)

    totalPossible = possibleDecrypts("35116433234167")
    print(totalPossible)

def possibleDecrypts(message):
    length = len(message)
    if length == 1:
        #Can only be 1
        return 1
    elif length == 2:
        #Can either be 2 digit number or 2 1 digit numbers
        if int(message) <= 26:
            return 2
        else:
            return 1

    totalPossible = possibleDecrypts(message[1:])

    if int(message[0:2]) <= 26:
        totalPossible += possibleDecrypts(message[2:])

    return totalPossible

main()
