#main() contains test cases for the containsSum() method
#containsSum() will return true if any 2 of the numbers in an array
#add up to k

def main():
    array = [10, 15, 3, 7]
    k = 17

    array2 = [11, 5, 2, 21, 53, 1000, 42]
    k2 = 44

    array3 = [5, 1, 3]
    k3 = 10
    
    print(containsSum(array, k))
    print(containsSum(array2, k2))
    print(containsSum(array3, k3))   

def containsSum(array, k):
    for i in range(0, (len(array) - 1)):
        for j in range(i+1, (len(array))):  
            tempValue = array[i] + array[j]
            if(tempValue == k):
                return True
    return False

main()
