/*Day 142 exam prep + i hate exam function*/
#include <stdio.h>
int i_hate_exams(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("I HATE EXAMS!😡\n");
    }
    return 0;
}
int main(void)
{
    int times;
    printf("How many times do you want to say 'I HATE EXAMS!'? ");
    scanf("%d", &times);
    i_hate_exams(times);
    return 0;
}
