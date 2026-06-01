/*day 127
random c quaestion chill and study for antigone quiz
C Problem — “Grade Tracker”
Write a C program that:

Asks the user how many quiz scores they have
Stores the scores in an array
Calculates:
average
highest score
lowest score
Prints a letter grade based on the average*/
#include <stdio.h>

int main(void)
{
    int num_scores;
    float sum = 0, average, highest, lowest;
    printf("How many quiz scores do you have? ");
    scanf("%d", &num_scores);
    float scores[num_scores];
    for (int i = 0; i < num_scores; i++)
    {
        printf("Enter score %d: ", i + 1);
        scanf("%f", &scores[i]);
        sum += scores[i];
    }
    average = sum / num_scores;
    highest = scores[0];
    lowest = scores[0];
    for (int i = 1; i < num_scores; i++)
    {
        if (scores[i] > highest)
        {
            highest = scores[i];
        }
        if (scores[i] < lowest)
        {
            lowest = scores[i];
        }
    }
    printf("Average: %.2f\n", average);
    printf("Highest: %.2f\n", highest);
    printf("Lowest: %.2f\n", lowest);
}