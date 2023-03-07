#include <stdio.h>

int main(void)
{
	int x;
	int y = 1;
	scanf("%d", &x);
	while (1) {
		
		printf("%d\n", y);
		y++;
		if (x < y) {
			break;
		}
	}
	
}