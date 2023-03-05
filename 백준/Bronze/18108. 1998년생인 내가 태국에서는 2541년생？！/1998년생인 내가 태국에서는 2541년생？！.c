#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int year;
    scanf("%4d", &year);
    int syear = year - 543;
    printf("%d", syear);
}