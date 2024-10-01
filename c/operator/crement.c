// increment and decrement operator
// ++a prefix or preIncrement
// a++ postfix or postIncrement

#include <stdio.h>

int main()
{
    printf("-----Q1------");
    int m = 10;
    int n, n1;
    n = ++m;
    n1 = m++;
    n--;
    --n1;
    n -= n1;
    printf(" \n Ans = %d \n", n);
    printf("-----Q2------");

    return 0;
}