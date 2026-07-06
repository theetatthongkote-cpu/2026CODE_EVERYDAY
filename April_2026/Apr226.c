/* day 92
using brocode "C Programming Full Course for free ⚙️"*/

#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int phone_num = 1991;
    float gpa = 3.0;
    float temperature = -9.5;
    double pi = 3.14159265;
    double e = 2.71828;
    char grade = 'A';
    char name[] = "Tigger";
    printf("hello, %.1f\n", gpa);
    printf("The tenperature outside is %.1f degress \n", temperature);
    printf("the value of pi %lf\n", pi);
    printf("the value of e %.4lf", e);
    printf("Your grade is %.c\n", grade);
    printf("Your Name is %.s\n", name);
}