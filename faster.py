import math
import timeit
import time

def calcDistance(ax, ay, bx, by):
    return math.sqrt(((ax-bx)**2)+((ay-by)**2))

def calcMidpoint(ax, ay, bx, by):
    return [(ax+bx)*0.5, (ay+by)*0.5]

def calcPi(runNumber="Test"):
    #print(runNumber)
    bx, by = 1, 0
    totArea = 0
    for i in range(1, 30):
        if i > 2:
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
            midpoint = [0.5, 0.5]
            midpointX, midpointY = midpoint[0], midpoint[1]
            midDistance = calcDistance(0, 0, midpointX, midpointY)
            normalizedX = 1
            normalizedY = 0
            triHeight = midDistance
            triWidth = calcDistance(0, 1, bx, by)
            triSize = (triHeight*triWidth)*0.5
            totArea += triSize
        else:
            midpoint = [0.5, 0.5]
            midpointX, midpointY = midpoint[0], midpoint[1]
            midDistance = calcDistance(0, 0, midpointX, midpointY)
            normalizedX = midpointX/midDistance
            normalizedY = midpointY/midDistance
            triHeight = 1-midDistance
            triWidth = calcDistance(0, 1, bx, by)
            triSize = (triHeight*triWidth)*0.5
            totArea += triSize
        
        bx, by = normalizedX, normalizedY
    return totArea*4

def library():
    runNumber = int(input("How many runs would you like to have? "))
    execution_time = timeit.timeit("calcPi()", globals=globals(), number=runNumber)
    print(f"Pi = {calcPi()}")
    print(f"Total Time Taken: {execution_time} Seconds")
    print(f"Average execution time over {runNumber} runs: {(execution_time/runNumber)*1000000:.5f} Microseconds")

def manual():
    runNumber = int(input("How many runs would you like to have? "))
    startT = time.time()
    for i in range(runNumber):
        calcPi(i)
    endT = time.time()
    print(f"Pi = {calcPi()}")
    print(f"Total Time Taken: {(endT-startT)} Seconds")
    # print(f"Acerage Time Taken: {((endT-startT)/runNumber)*1000000} Microseconds")
    print(f"Average execution time over {runNumber} runs: {((endT-startT)/runNumber)*1000000:.5f} Microseconds")
    
def main():
    method = int(input("How would you like to measure time (1/2)\n    1. Library (timeit)\n    2. Manual\n"))
    if method == 1:
        library()
    else:
        manual()

main()