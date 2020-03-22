#main() contains test cases for areWellFormedBrackets()
#The method will find pairs that are ajacent to eachother and remove them
#When the string has nothing left, it must be well formed
#Remove the comment on the print() in areWellFormedBrackets() for a better idea
#about how it works

def main():
    print(areWellFormedBrackets("([])[]({})"))
    print(areWellFormedBrackets("([)]"))
    print(areWellFormedBrackets("((()"))

def areWellFormedBrackets(string):

    if(len(string) == 0):
        return True
    elif(len(string) == 1):
         return False

    #print(string)

    foundPair = False
    newString = ""
    for i in range (0, len(string)-1):
        if(isOpenPartner(string[i], string[i+1])):
            #remove those two, go again
            newString += string[:i]
            newString += (string[(i+2):])
            foundPair = True
            break

    if(foundPair):
        return areWellFormedBrackets(newString)
    else:
        return False

def isOpenPartner(openB, closedB):
    if(openB == "(" and closedB == ")"):
       return True

    if(openB == "[" and closedB == "]"):
        return True
    
    if(openB == "{" and closedB == "}"):
        return True
    
    return False
    
main()
