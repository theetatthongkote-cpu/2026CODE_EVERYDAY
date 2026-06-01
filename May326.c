/*Day 123
CS50 */

#include <stdio.h>
int main(void)
{
    int height, i, j, k, l;
    height = 4;
    for (i = 0; i < height; i++)
    {
        for (j = 0; j < height - i - 1; j++)
        {
            printf(" ");
        }
        for (k = 0; k <= i; k++)
        {
            printf("*");
        }

        printf("  ");
        for (l = 0; l <= i; l++)
        {
            printf("*");
        }
        printf("\n");
    }
}