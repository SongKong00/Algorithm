#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    double first, second, third;
    scanf("%lf %lf %lf", &first, &second, &third);
    printf("%.f", first+second+third);
    return 0;
}