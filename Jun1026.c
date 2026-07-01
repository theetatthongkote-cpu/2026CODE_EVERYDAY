// day 158
// caesar in cs50
#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

void cipher(string plaintext, int key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (isdigit(argv[1][i]) == 0)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);
    while (key > 26)
    {
        key -= 26;
    }

    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");
    cipher(plaintext, key);
    printf("\n");
}

void cipher(string plaintext, int key)
{
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (isupper(plaintext[i]))
            {
                printf("%c", (plaintext[i] - 'A' + key) % 26 + 'A');
            }
            else
            {
                printf("%c", (plaintext[i] - 'a' + key) % 26 + 'a');
            }
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
}
