#include <stdio.h>
#include <math.h>
#include <time.h>

int main() {
    double resolution = 0.00000001;            // Resolution, this is what I recommend for a short runtime and ok precision
    double y = 1;                               // Default starting y position
    double total=0;                             // Keeps track of the total

    clock_t start, end;                         // All the time stuff I found online
    double cpu_time_used;
    start = clock();

    for (double x = 0; x < 1; x+=resolution) {
        y = (sqrt(1-x*x));                      // Finds the y coordinate of x based on a semicircle graph
        total += y;                             // Adds the y position to the total
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    double pi = (total*4)*resolution;
    printf("Pi Approximation: %.10f\n", pi);    // Prints Results
    printf("Time Taken: %f\n", cpu_time_used);
    return 0;
} 