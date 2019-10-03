#include<stdio.h>
#include<conio.h>

#define MAX 100

int main()
{
	int a[MAX], n, i, j, k;
	clrscr();

	printf("Enter the size of array (max %d): ", MAX);
		scanf("%d", &n);
	printf("Enter the array: ");
	for(i = 0; i < n; i++)
		scanf("%d", a[i]);


	getch();
	return 0;
}