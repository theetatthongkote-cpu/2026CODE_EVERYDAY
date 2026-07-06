/*
day 128
credit in cs50 pt 1*/
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