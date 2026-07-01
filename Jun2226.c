// day 169
// today i learned how to argv and argc aswell as how to compare strings using strcmp in harvard's cs50 course.
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("Hello there! %s\n", argv[1]);
    }
    else
    {
        printf("./test name\n");
        return 1;
    }
    string strings[] = {"red", "blue", "green", "yellow"};
    string s = get_string("String: ");
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(strings[i], s) == 0)
        {
            printf("Found %s!\n", s);
            return 0;
        }
    }
    printf("%s is not found\n", s);
    return 1;
}
