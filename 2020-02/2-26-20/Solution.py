#main() contains test cases for greatestNonAdjacentSum()
#This problem was fun to think about! Ended up finding a recursive solution
#even though I couldn't get it to run in O(N) time and constant space.

def main():
    print(greatestNonAdjacentSum([0,1,2,3,4,5]))
    print(greatestNonAdjacentSum([2,4,6,2,5]))
    print(greatestNonAdjacentSum([5,1,1,5]))

def greatestNonAdjacentSum(array):
    if(len(array) == 0): #If nothing is in the array, there is no sum
        return 0
    if(len(array) == 1): #If there is only 1 element, we can return that element
        return array[0]
    elif(len(array) == 2): #If there are two elements, check which one is greater and return it
        if(array[0] > array[1]):
            return array[0]
        else:
            return array[1]

    #The answer will always include the first or second element
    #Check both recursively, then check which one is greater
    #I've also excluded the next element because they would be adjacent
    sum1 = array[0] + greatestNonAdjacentSum(array[2:])
    
    sum2 = array[1] + greatestNonAdjacentSum(array[3:])

    if(sum1 > sum2):
        return sum1
    else:
        return sum2
    
main()
