import math
import time

def calcDistance(ax, ay, bx, by):
    return math.sqrt(((ax-bx)**2)+((ay-by)**2))

def calcMidpoint(ax, ay, bx, by):
    return [(ax+bx)*0.5, (ay+by)*0.5]

def main():
    bx, by = 1, 0
    totArea = 0
    startTime = time.time()
    for i in range(1, 30):
        if i > 2:
            print("Run", i)
            midpoint = calcMidpoint(0, 1, bx, by)
            midpointX, midpointY = midpoint[0], midpoint[1]
            midDistance = calcDistance(0, 0, midpointX, midpointY)
            normalizedX = midpointX/midDistance
            normalizedY = midpointY/midDistance
            triHeight = 1-midDistance
            triWidth = calcDistance(0, 1, bx, by)
            triSize = (triHeight*triWidth)*0.5
            totArea += triSize*(2**(i-2))
        elif i == 1:
            print("Run", i)
            midpoint = [0.5, 0.5]
            midpointX, midpointY = midpoint[0], midpoint[1]
            midDistance = calcDistance(0, 0, midpointX, midpointY)
            print(f"Midpoint: [{midpointX}, {midpointY}]")
            print("Mid Distance:", midDistance)
            normalizedX = 1
            normalizedY = 0
            triHeight = midDistance
            triWidth = calcDistance(0, 1, bx, by)
            triSize = (triHeight*triWidth)*0.5
            totArea += triSize
        else:
            print("Run", i)
            midpoint = [0.5, 0.5]
            midpointX, midpointY = midpoint[0], midpoint[1]
            midDistance = calcDistance(0, 0, midpointX, midpointY)
            print(f"Midpoint: [{midpointX}, {midpointY}]")
            print("Mid Distance:", midDistance)
            normalizedX = midpointX/midDistance
            normalizedY = midpointY/midDistance
            triHeight = 1-midDistance
            triWidth = calcDistance(0, 1, bx, by)
            triSize = (triHeight*triWidth)*0.5
            totArea += triSize
        
        print("Triangle Height:", triHeight)
        print("Triangle Width:", triWidth)
        print("Triangle Size:", triSize, "\n")
        bx, by = normalizedX, normalizedY
    endTime = time.time()
    print(totArea*4)
    print("Total Runtime:", endTime-startTime)

        

main()
