/*Day 143 exam prep + i wanna sleep function*/
#include <stdio.h>
int i_hate_exams(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("I wanna sleep😴\n");
    }
    return 0;
}
int main(void)
{
    int times;
    printf("I wanna sleep😴 ");
    scanf("%d", &times);
    i_hate_exams(times);
    return 0;
}
