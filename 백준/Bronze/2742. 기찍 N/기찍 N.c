#include <stdio.h>

int main(void)
{
	int x;

	scanf("%d", &x);
	int k = x;
	for (int i = 1; i <= x; i++) {
		printf("%d\n", k);
		k--;
	}
	
}