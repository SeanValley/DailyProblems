#main() contains test cases for longestSubstring()
#This algorithm worked on my first attempt and I didn't debug until I was done writing!
#It checks starting with each character of the string and adds on each consecutive character
#When it hits the amount of unique characters that is greater than k, it checks if the string
#it built is larger than the largest string so far
#if it is, it replaces it. At the end of the string, it returns the largest substring it found.

def main():
    print(longestSubstring("abcba", 2))
    print(longestSubstring("teststring", 2))
    print(longestSubstring("hereiwilltestforthreecharacters", 3))

#returns longest substring from string s, where there are at most k distinct characters
def longestSubstring(s, k):
    longestLength = 0
    longestString = ""

    for i in range(0, len(s)):
        uniqueCharacters = s[i]
        newString = ""
        for j in range(i, len(s)):
            if(s[j] not in uniqueCharacters):
                uniqueCharacters += s[j]

            if(len(uniqueCharacters) > k):
                break
            else:
                newString += s[j]
        if(len(newString) > longestLength):
            longestString = newString
            longestLength = len(newString)

    return longestString
    
main()
