/*
day 131
using scanf
absolute basics😪*/
/*
What is your age?
What is your GPA?
What is your first name? */

#include <stdio.h>
int main(void)
{
    int age;
    float gpa;
    char name[20];
    printf("What is your age? ");
    scanf("%i", &age);
    printf("What is your GPA? ");
    scanf("%f", &gpa);
    printf("What is your first name? ");
    scanf("%s", name);
    printf("Your age is %d, your GPA is %.2f, and your name is %s.\n", age, gpa, name);
}