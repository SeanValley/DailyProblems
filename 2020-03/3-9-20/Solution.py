#main() contains test cases for minClassrooms()

def main():
    print(minClassrooms([(4, 6), (1, 4), (5, 10)]))
    print(minClassrooms([(1, 5), (2, 4), (4, 6), (3, 4)]))

#returns the minimum amount of classrooms for the classes taking place during classes hours
def minClassrooms(classes):
    if(len(classes) == 1):
       return 1
    
    startingHours = []
    endingHours = []
    for classHours in classes:
        startingHours.append(classHours[0])
        endingHours.append(classHours[1])

    startingHours = mergeSort(startingHours)
    endingHours = mergeSort(endingHours)


    maxOngoingClasses = 1
    ongoingClasses = 1
    startingIndex = 1
    endingIndex = 0
    done = False

    while not done:
        if startingHours[startingIndex] < endingHours[endingIndex]:
            ongoingClasses += 1
            startingIndex += 1
        else:
            ongoingClasses -= 1
            endingIndex += 1

        if ongoingClasses > maxOngoingClasses:
            maxOngoingClasses = ongoingClasses

        if startingIndex == len(startingHours):
            done = True
    
    
    return maxOngoingClasses

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
