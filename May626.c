/* day 126
cs50 cash problem set 1
fully */
// #include <cs50.h>
#include <stdio.h>

int quarter(int c);
int dime(int c);
int nickel(int c);

int main(void)
{
    int change;

    do
    {
        change = get_int("Change owed: ");
    } while (change < 0);

    int quarters = quarter(change);
    change = change - (25 * quarters);

    int dimes = dime(change);
    change = change - (10 * dimes);

    int nickels = nickel(change);
    change = change - (5 * nickels);

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
