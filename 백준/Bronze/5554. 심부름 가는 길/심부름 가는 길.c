#include <stdio.h>

int main()
{
	int one = 0, two = 0, three = 0, four = 0, all = 0, min = 0, sec = 0;
	scanf("%d\n%d\n%d\n%d\n", &one, &two, &three, &four);

	all = one + two + three + four;
	min = all / 60;
	sec = all % 60;
	
	printf("%d\n%d", min, sec);
}