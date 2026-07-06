/*Day 136 Mini Exercise — “Simple Calculator”*/

#include <stdio.h>
int main(void)
{
    int a, b;
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);
    printf("Sum: %d\n", a + b);
    printf("Difference: %d\n", a - b);
    printf("Product: %d\n", a * b);
    printf("Quotient: %.2f\n", (float)a / b);
    return 0;
}