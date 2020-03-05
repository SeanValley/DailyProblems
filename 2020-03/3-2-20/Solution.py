#estimatePi() will estimate Pi within about 3 decimal places
#I describe the algorithm below

from random import random

def estimatePi():
    totalIn = 0
    totalPoints = 2000000

    #For every loop, generate a random points in range (-1, 1)
    #Check if that point lies within the circle
    #Pi will be aproxamitely equal to 4 * (pointsInCircle / totalPoints)
    #Increase total points for higher percision
    #I found 2,000,000 points gives around 3 decimal places of accuracy
    for i in range(0, totalPoints):
        randomX = (random() * 2) - 1
        randomY = (random() * 2) - 1
        isInCircle = isPointWithinCircle(randomX, randomY, 1)
        if(isInCircle):
            totalIn += 1

    piEstimate = 4 * (totalIn / totalPoints)
    print(piEstimate)

#returns whether point (x,y) is within circle centered at (0,0) with r radius
def isPointWithinCircle(x, y, r):
    
    if((x**2) + (y**2) <= (r**2)):
        return True
    else:
        return False
    
estimatePi()
