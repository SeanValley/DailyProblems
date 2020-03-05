#main() contains test cases for the findLowestNonExistentInt() method
#I had a bit of trouble with this problem. I was only able to reduce
#my algorithm's time complexity to O(nlogn)
#I'm sure there's a better way to solve this problem, I'll have to check the solution
#and come back to it

def main():
    testArr = [2, 7, 18, 52, 9, 1, 2]
    lowest = findLowestNonExistentInt(testArr)

    testArr2 = [3, 3, 5]
    lowest2 = findLowestNonExistentInt(testArr2)

    testArr3 = [3, 4, -1, 1]
    lowest3 = findLowestNonExistentInt(testArr3)

    testArr4 = [1, 2, 0]
    lowest4 = findLowestNonExistentInt(testArr4)
    
    print(lowest)
    print(lowest2)
    print(lowest3)
    print(lowest4)

def findLowestNonExistentInt(array):
    array = mergeSort(array)
    lowest = 1
    for i in range(0, len(array)):
        if array[i] == lowest:
            lowest += 1
        elif i != 0 and array[i] != array[(i-1)]:
            return lowest
    #If it goes through the entire array without finding the answer, it must be 1 higher
    #than the last int in the array
    return array[len(array) - 1] + 1
            

def mergeSort(array):
    newArray = array
    if len(newArray) > 1:
        mid = len(newArray) // 2
        leftArray = newArray[:mid]
        rightArray = newArray[mid:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = 0
        j = 0
        
        index = 0
        
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
              newArray[index] = leftArray[i]
              i += 1
            else:
                newArray[index] = rightArray[j]
                j += 1
            index += 1

        while i < len(leftArray):
            newArray[index] = leftArray[i]
            i += 1
            index += 1

        while j < len(rightArray):
            newArray[index]=rightArray[j]
            j += 1
            index += 1
    return newArray
    
main()
