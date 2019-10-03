#include<stdio.h>
#include<conio.h>

#define MAX 100

int main()
{
	int a[MAX], n, i, j, tmp;
	clrscr();

	printf("Enter the size of array (max %d): ", MAX);
		scanf("%d", &n);
	printf("Enter the array: ");
	for(i = 0; i < n; i++)
		scanf("%d", &a[i]);

	for(i = 1; i < n; i++)
	{

		for(j = i; j > 0 && a[j-1] > a[j]; j--)
		{
			tmp = a[j];
			a[j] = a[j-1];
			a[j-1] = tmp;
		}
	}

	printf("The sorted array is: \n");
	for(i = 0; i < n; i++)
		printf("%d, ", a[i]);



	getch();
	return 0;
}