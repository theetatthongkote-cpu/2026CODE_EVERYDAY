// day 147 warm up and guessing number game
#include <stdio.h>
#include <stdlib.h>

int main(void)
{

    do
    {
        int number, guess;
        number = 7; // number to guess
        printf("Guess the number between 1 and 10: ");
        scanf("%d", &guess);
        if (guess == number)
        {
            printf("Congratulations! You guessed the number.");
            break;
        }
        else if (guess < number)
        {
            printf("Too low! Try again.\n");
        }
        else if (guess > number)
        {
            printf("Too high! Try again.\n");
        }
    } while (1); // infinite loop until the correct number is guessed
}
