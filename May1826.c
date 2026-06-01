/*Day 137 Mini Exercise — ““Positive, Negative, or Zero”*/

#include <stdio.h>
int main(void)
{
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);
    if (num > 0)
        printf("Positive integer");
    else if (num < 0)
        printf("Negative integer");
    else
        printf("Zero");
    return 0;
}