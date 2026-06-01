/* day 125
cs50 cash problem set 1
almost finished*/
#include <stdio.h>

int quarter(int c);
int dime(int c);
int nickel(int c);

int main(void)
{
    int change;

    do
    {
        printf("Change owed: ");
        if (scanf("%d", &change) != 1)
        {
            return 1;
        }
    } while (change < 0);

    int quarters = quarter(change);
    change -= 25 * quarters;

    int dimes = dime(change);
    change -= 10 * dimes;

    int nickels = nickel(change);
    change -= 5 * nickels;

    int coins = quarters + dimes + nickels + change;
    printf("%i\n", coins);

    return 0;
}

int quarter(int c)
{
    return c / 25;
}
int dime(int c)
{
    return c / 10;
}
int nickel(int c)
{
    return c / 5;
}
