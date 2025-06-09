#include <stdio.h>
#include "math_utils.h"
#define A 5
#define B 3
#define add(a,b) A+b

int main() 
{
    //ADD 2 values
    printf("Add: %d\n", add(A, B));
    printf("Subtract: %d\n", subtract(A, B));
    return 0;
}
