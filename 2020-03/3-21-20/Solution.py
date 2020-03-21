#main() contains a test case for the median finder
#stream(x) streams the next int into the median finder.
#From there, it inserts it into its running list, sorted
#getMedian() will find the median of the current sorted list

import bisect

def main():
    stream = [2, 1, 5, 7, 2, 0, 5]
    medianFinder = MedianFinder()
    for i in stream:
        medianFinder.stream(i)
        print(medianFinder.getMedian())

class MedianFinder:
    def __init__(self):
        self.sortedList = []

    def stream(self, x):
        bisect.insort(self.sortedList, x)

    def getMedian(self):
        length = len(self.sortedList)
        if(length == 0):
            return 0
        elif(length == 1):
            return self.sortedList[0]
        elif(length % 2 == 0):
            firstIndex = self.sortedList[(length // 2) - 1]
            secondIndex = self.sortedList[(length // 2)]
            return (firstIndex + secondIndex) / 2
        else:
            return self.sortedList[(length // 2) - 1]

main()
