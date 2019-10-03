#include<stdio.h>
#include<conio.h>

void main()
{
	int a[10], i, j, n, tmp;
	clrscr();
	printf("Enter the number of elements: ");
	scanf("%d", &n);
	printf("Enter the values of array (max 10): ");
	for(i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
	}

	for(i = 0; i < n; i++)
		for(j = 0; j < n; j++)
			if(a[j] > a[j+1])
			{
				tmp = a[j];
				a[j] = a[j+1];
				a[j+1] = tmp;
			}
	printf("The sorted array is:" );
	for (i = 0; i < n; i++)
		printf("%d, ", a[i]);


	getch();
}