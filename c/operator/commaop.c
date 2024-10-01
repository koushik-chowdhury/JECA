#include <stdio.h>
int main()
{
    // int a = (1, 2, 3, 4);
    int b, c, d, e;
    d = (b = 1, d = 2, c = 3, d + b + c);

    // printf("%d", a);
    printf("\n");
    printf("%d", d);

    return 0;
}