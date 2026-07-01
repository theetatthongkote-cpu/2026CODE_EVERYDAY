// day 169
// today i learned how "typedef struct" and implemented it into my program "test.c" in harvard's cs50 course.
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// example of a struct and using persons and people
/*
 typedef struct
{
  string name;
  string number;}
  person;
  */
#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string color;
} favcolors;

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
    favcolors people[4];
    people[0].name = "Adam";
    people[0].color = "red";

    people[1].name = "Beth";
    people[1].color = "blue";

    people[2].name = "Carl";
    people[2].color = "green";

    people[3].name = "Darius";
    people[3].color = "yellow";

    string s = get_string("Name: ");
    for (int i = 0; i < 4; i++)
    {
        if (strcmp(people[i].name, s) == 0)
        {
            printf("Favorite color: %s!\n", people[i].color);
            return 0;
        }
    }
    printf("%s is not found\n", s);
    return 1;
}
