#main() contains a test case for calling staircasePermutations
#I wasn't able to get it working with arbitrary amounts of steps allowed but I plan on
#coming back and figuring it out!

import sys

def main():
    print(staircasePermutations(4))
#   print(bonusSPs(4, [1,2]))

#n is the amount of steps on the staircase
def staircasePermutations(n):
    if(n <= 0):
        return 0
    elif(n == 1):
        return 1
    elif(n == 2):
        return 2
    else:
        totalPermutations = 0
        totalPermutations += staircasePermutations(n-1) #Going up 1 step
        totalPermutations += staircasePermutations(n-2) #Going up 2 steps
        return totalPermutations

#n is the amount of steps on the staircase, array is a set of all possible steps that can be
#taken at once. (Not Working)
#def bonusSPs(n, array):
#    lowestStep = getLowest(array)
#    if(n < lowestStep):
#        return 0
#    else:
#        totalPermutations = 0
#        for element in array:
#            if(element == n):
#                return 1 + bonusSPs((n - element), array)
#            else:
#                totalPermutations += bonusSPs((n - element), array)
#        return totalPermutations

#Returns lowest element in an array
def getLowest(array):
    lowest = sys.maxsize
    for element in array:
          if(element < lowest):
              lowest = element
    return lowest

main()
