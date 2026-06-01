/*Day 142 exam prep + weather checker*/
#include <stdio.h>
int main(void)
{
    int temp;
    printf("Enter the temperature in Celsius: ");
    scanf("%d", &temp);
    if (temp > 30)
        printf("It's hot outside!🔥");
    else if (temp > 20)
        printf("It's warm outside!☀️");
    else if (temp > 10)
        printf("It's cool outside!🍃");
    else
        printf("It's cold outside!❄️");
    return 0;
}
