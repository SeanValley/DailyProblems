#main() contains a test case for calling testFunction() after 2 seconds (2000 milliseconds)

import time

def main():
    print("Calling delay function...")
    delayFunc(testFunction, 2000)

#f is the function to be called after n milliseconds
def delayFunc(f, n):
    print("Delay Function was called...")
    seconds = n / 1000
    time.sleep(seconds)
    f()

def testFunction():
    print("Test function was called.")

main()
