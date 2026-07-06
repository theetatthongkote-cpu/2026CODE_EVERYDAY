// day 67
/*
========================================
Learning Log – March 8
Course: CS50x Introduction to Computer Science
Language: C
========================================

Topics Learned:
1. Functions in C
2. Returning values from functions
3. do-while loops
4. for loops
5. Input validation
6. Program structure and abstraction
*/

// #include <stdio.h>

// Function prototypes
int get_positive_int(void);
void meow(int n);

int main(void)
{
    // Get a valid positive integer from the user
    int n = get_positive_int();

    // Call the meow function with the user's number
    meow(n);
}

/*
----------------------------------------
Function: get_positive_int
Purpose:
    Ask the user for a number until
    they enter a positive integer.

Concepts learned:
- do-while loop
- input validation
- returning values
----------------------------------------
*/

int get_positive_int(void)
{
    int n;

    // Runs at least once
    do
    {
        printf("Enter a positive number: ");
        scanf("%d", &n);
    } while (n < 1);

    return n;
}

/*
----------------------------------------
Function: meow
Purpose:
    Print "meow" n times.

Concepts learned:
- parameters
- for loops
----------------------------------------
*/

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}

/*
----------------------------------------
Key Concepts From Today
----------------------------------------

1. Functions
   Functions break programs into smaller pieces.

2. Return Values
   A function can send a value back using:

       return value;

   Example:
       int get_positive_int(void)
       {
           return n;
       }

3. do-while Loop
   Runs at least once before checking the condition.

       do
       {
           code
       }
       while (condition);

4. for Loop
   Used when the number of iterations is known.

       for (int i = 0; i < n; i++)

5. Abstraction
   Separating tasks into different functions.

   main() → controls the program
   get_positive_int() → handles input
   meow() → handles output

----------------------------------------
End of March 8 Learning Log
----------------------------------------
*/