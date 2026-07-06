// Day 154
//  cs50's scrabble problem set 2
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
int calculate_score(string word);
int POINTS[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int main(void)
{
    string player1, player2;
    player1 = get_string("Player 1: ");
    player2 = get_string("Player 2: ");

    int score1 = calculate_score(player1);
    int score2 = calculate_score(player2);
    if (score1 > score2)
    {
        printf("Player1 wins!\n");
    }
    else if (score1 == score2)
    {
        printf("Ties!\n");
    }
    else
    {
        printf("Player2 wins!\n");
    }
}
int calculate_score(string word)
{
    int m, score = 0, i, n;
    for (i = 0, n = strlen(word); i < n; i++)
    {
        if (isalpha(word[i]) && word[i] > 64 && word[i] < 91)
        {
            score += POINTS[word[i] - 65];
        }

        if (isalpha(word[i]) && word[i] > 96 && word[i] < 123)
        {
            score += POINTS[word[i] - 97];
        }
        else
        {
            score += 0;
        }
    }
    return score;
}
