#include <stdio.h>

int main()
{
	int stone = 0;
	scanf("%d", &stone);
	if (stone % 2 == 0) {
		printf("CY");
	}
	else {
		printf("SK");
	}
}