/*Day 143 exam prep + discriminant + quadratic formula*/
#include <stdio.h>
#include <math.h>
int main(void)
{
    double a, b, c;
    printf("Enter coefficients a, b, and c: ");
    scanf("%lf %lf %lf", &a, &b, &c);
    double discriminant = b * b - 4 * a * c;
    if (discriminant > 0)
    {
        double root1 = (-b + sqrt(discriminant)) / (2 * a);
        double root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("The roots are %.2lf and %.2lf\n", root1, root2);
    }
    else if (discriminant == 0)
    {
        double root = -b / (2 * a);
        printf("The root is %.2lf\n", root);
    }
    else
    {
        printf("No real roots exist.\n");
    }
    return 0;
}