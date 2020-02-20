#main() contains test cases for the solutionArray() and BonusArray() method
#solutionArrays' values are equal to every other index's value in the initial
#array multiplied together
#Not sure if the bonus solution is a true solution because it still has to
#loop over the new array to multiply to each index.

def main():
    array1 = [1, 2, 3, 4, 5]
    array2 = [3, 2, 1]
    array3 = [10, 15, 3, 7]

    print("solutionArray method:")
    print(solutionArray(array1))
    print(solutionArray(array2))
    print(solutionArray(array3))
    #Expected output: [315, 210, 1050, 450]
    print("bonusSolutionArray method:")
    print(bonusSolutionArray(array1))
    print(bonusSolutionArray(array2))
    print(bonusSolutionArray(array3))


def solutionArray(initialArray):
    newArray = [None]*len(initialArray)
    
    for i in range(0, len(initialArray)):
        newValue = initialArray[0]
        if(i == 0):
            newValue = 1
        for j in range(1, len(initialArray)):
            if(i != j):
              newValue *= initialArray[j]
        newArray[i] = newValue
    return newArray

def bonusSolutionArray(initialArray):
    newArray = [1]*len(initialArray)

    for i in range(0, len(initialArray)):
        for j in range(0, len(newArray)):
            if(i != j):
                newArray[j] *= initialArray[i]
    return newArray

main()
