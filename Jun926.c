// day 157
// readability in cs50
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int letter_count(string input);
int word_count(string input);
int sentence_count(string input);
int indexed(int sentences, int words, int letters);

int main(void)
{
    string input = get_string("Text: ");

    int letters = letter_count(input);
    int words = word_count(input);
    int sentences = sentence_count(input);
    int index = indexed(sentences, words, letters);

    if (index < 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
        return 0;
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int letter_count(string input)
{
    int letters = 0;
    for (int i = 0; i < strlen(input); i++)
    {
        if (isalpha(input[i]))
            letters++;
    }
    return letters;
}

int word_count(string input)
{
    int words = 0;
    for (int j = 0; j < strlen(input); j++)
    {
        if (input[j] == ' ')
            words++;
    }
    return words + 1;
}

int sentence_count(string input)
{
    int sentences = 0;
    for (int k = 0; k < strlen(input); k++)
    {
        if (input[k] == '.' || input[k] == '?' || input[k] == '!')
            sentences++;
    }
    return sentences;
}

int indexed(int sentences, int words, int letters)
{
    return round(0.0588 * letters / words * 100 - 0.296 * sentences / words * 100 - 15.8);
}
