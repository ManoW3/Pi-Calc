#include <stdio.h>
#include <math.h>
#include <time.h>
#include <locale.h>

long double calcDistance (long double ax, long double ay, long double bx, long double by) {
    return sqrt(((ax-bx)*(ax-bx))+((ay-by)*(ay-by)));
}

// Not the most efficient but I don't have internet so I can't search up how to return array
long double midpointX (long double ax, long double bx) {
    return (ax+bx)*0.5;
}

long double midpointY (long double ay, long double by) {
    return (ay+by)*0.5;
}

long double calcPi () {
    int size = 1;
    // Sets starting point
    long double bx = size;
    long double by = 0;
    long double totArea = size*size*0.5;
    for (int i = 0; i < 30; i++) {
        // Finds midpoint
        long double midX = midpointX(0, bx);
        long double midY = midpointY(size, by);
        // Normalizes to be on circle
        long double midDistance = calcDistance(0, 0, midX, midY);
        long double normalizedY = (midY/midDistance)*size;
        long double normalizedX = (midX/midDistance)*size;
        // Calculates triangle size
        long double triHeight = size-midDistance;
        long double triWidth = calcDistance(0, size, bx, by);
        long double triSize = (triHeight*triWidth)*0.5;
        // Multiplies by 2^i because each time, there are double the amount of each triangle
        totArea += triSize*(pow(2, (i)));
        // Sets the point to the normalized point
        bx = normalizedX;
        by = normalizedY;
    }
    // Multiplies by 4
    return (totArea*4)/(size*size);

}

int main() {
    setlocale(LC_NUMERIC, "");                  // For better formatting when printing
    // Number of runs
    int runNumber = 100000;
    clock_t start, end;                         // All the time stuff I found online
    double cpu_time_used;
    start = clock();
    
    // Main loop for time testing
    for (int i = 0; i < runNumber; i++) {
        calcPi();
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Pi: %.14Lf\n", calcPi());
    printf("Time Taken: %f Seconds for %'d runs\n", cpu_time_used, runNumber);
    float timePerRun = (cpu_time_used/runNumber)*1000000;
    printf("Average Time Taken: %f Microseconds\n", timePerRun);

    return 0;
} 