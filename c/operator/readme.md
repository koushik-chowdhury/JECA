## Arithmatic operator on integer datatype

```c
#include<stdio.h>
int main()
{
    int x = 10, y = 5;
    printf("Sum = %d \n", x + y);
    printf("Dif = %d \n", x - y);
    printf("Prod = %d \n", x * y);
    printf("Quotient = %d \n", x / y);
    printf("remainder = %d \n", x % y);
    return 0;
}
```
## Code Breakdown

- `int x = 10, y = 5` <br>
Defines two integer variables, `x` and `y`, where `x = 10` and `y = 5`.

## Operator 
- `+` (Addition): Adds two numbers.<br> **Example:** `x + y = 15`
- `-` (Substraction): Subtracts one number from another.<br> **Example:** `x - y = 10`
- `*` (Multiplication): Multiplies two numbers.<br> **Example:** `x * y = 50`
- `-` (Division): Divides two numbers and returns the quotient (integer part of the division). <br> **Example:**`x / y = 2`
- `%` (Modulo): Returns the remainder of the division of two numbers.<br> **Example:** `x % y = 0`


## Arithmatic operator on Float datatype
```c
#include<stdio.h>
int main()
{
    float x = 10, y = 4;
    printf("Sum = %f \n", x + y);
    printf("Dif = %f \n", x - y);
    printf("Prod = %f \n", x * y);
    printf("Quotient = %f \n", x / y);
    return 0;
}
```
## Code Breakdown

- `float x = 10, y = 4` <br>
Defines two float variables, `x` and `y`, where `x = 10` and `y = 4`.


## Operator 
- `+` (Addition): Adds two numbers.<br> **Example:** `x + y = 15.000000`
- `-` (Substraction): Subtracts one number from another.<br> **Example:** `x - y = 6.000000`
- `*` (Multiplication): Multiplies two numbers.<br> **Example:** `x * y = 50.000000`
- `-` (Division): Divides two numbers . <br> **Example:** `x / y = 2.500000`
    
    - We can customize fraction part of float data type
    ```c
    printf("%.2f", x / y);
    ```

> [!NOTE]  
> We can't do any Arithmatic operation on diffrent DataType like -

```c
int x = 10, y = 4;
printf("%f", x / y);
```