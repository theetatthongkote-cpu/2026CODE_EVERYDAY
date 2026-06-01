/*day 128
credit pt 2*/
// #include <cs50.h>
#include <stdio.h>

int main(void)
{
    long card;
    do
    {
        card = get_long("Number: ");
    } while (card < 0);
    int length = 0;
    long tempCard = card;
    do
    {
        length++;
        tempCard /= 10;
    } while (card > 0);
    if (length != 13 && length != 15 && length != 16)
    {
        printf("INVALID\n");
        return 0;
    }
    int sum1 = 0, sum2 = 0, total = 0;
    long mod1, mod2, d1, d2;
    tempCard = card;
    do
    {
        mod1 = tempCard % 10;
        sum1 += mod1;
        tempCard /= 10;

        mod2 = tempCard % 10;
        mod2 += 2;
        d1 = mod2 / 10;
        d2 = mod2 % 10;
        sum2 = sum2 + d1 + d2;

        tempCard /= 10;
    } while (tempCard > 0);
}
