#include <stdio.h>

int main(void)
{
	int x,i,j;
	scanf("%d", &x);
	for (i = 0; i <x; i++) {
		for (j = 0; j <= i; j++) {
			printf("*");
			
		}printf("\n");
	}
	
}