/*💻 Day 135 Mini C Exercise — “Square Function”*/

#include <stdio.h>
int square(int x);
int main(void)
{
    int number;
    printf("Enter an integer: ");
    scanf("%d", &number);
    printf("The square of %d is %d.\n", number, square(number));
    return 0;
}
int square(int x)
{
    return x * x;
}