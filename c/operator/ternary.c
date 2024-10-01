#include<stdio.h>
int main()
{
int x, y, max;
printf("Enter values of x and y : ");
scanf("%d%d", &x, &y);
max = x > y ? x:y;
printf("Larger of %d and %d is %d", x, y, max);
return 0;
}