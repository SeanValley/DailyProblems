#main() contains test cases for encode() and decode()

def main():
    stringToEncode = "AAAABBBCCDAA"
    print("Original:", stringToEncode)
    encodedString = encode(stringToEncode)
    print("Encoded:", encodedString)
    decodedString = decode(encodedString)
    print("Decoded Again:", decodedString)

    print("\n")

    stringToEncode = "BDDEEEAACAAAAEEEEEEE"
    print("Original:", stringToEncode)
    encodedString = encode(stringToEncode)
    print("Encoded:", encodedString)
    decodedString = decode(encodedString)
    print("Decoded Again:", decodedString)
    

def encode(string):
    encodedString = ""
    
    currentChar = ''
    charsInARow = 1
    for char in string:
        if(currentChar == ''):
            currentChar = char
        elif(char == currentChar):
            charsInARow += 1
        else:
            encodedString += str(charsInARow)
            encodedString += currentChar
            currentChar = char
            charsInARow = 1

    encodedString += str(charsInARow)
    encodedString += currentChar
    return encodedString

def decode(string):
    decodedString = ""
    
    for i in range(0, ((len(string)//2))):
        amount = int(string[i*2])
        char = string[(i*2) + 1]
        
        for j in range(0, amount):
            decodedString += char

    return decodedString

main()
