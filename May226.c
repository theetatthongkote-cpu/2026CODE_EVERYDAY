// day 122
//  cs50 calculator
// pyramid
#include <stdio.h>
// #include <cs50.h>

/*int main(void)
{
    int x, y;
    x = get_int("What is x: ");
    y = get_int("What is y: ");
    printf("%i\n", x + y);
}*/

#include <stdio.h>

int main(void)
{
    int height = 5; // you can change this later

    for (int i = 0; i < height; i++)
    {
        // print spaces
        for (int j = 0; j < 4 - i - 1; j++)
        {
            printf(" ");
        }

        // print hashes
        for (int k = 0; k <= i; k++)
        {
            printf("*");
        }

        // move to next line
        printf("\n");
    }
}

#include <stdio.h>

int main(void)
{
    int height = 4;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}