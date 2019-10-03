#include<stdio.h>
#include<conio.h>

#define SIZE 100

int main()
{
	int a[SIZE], n, i, j, smallest = 32767, pos;

	clrscr();
	printf("Enter the size of the array (Max %d): \n", SIZE);
	scanf("%d", &n);
	for(i = 0; i < n; i++)
		scanf("%d", &a[i]);

	for(i = 0; i < n; i++)
	{
		for(j = i; j < n; j++)
		{
			if(a[j]<smallest)
			{
				smallest = a[j];
				pos = j;
			}
		}
		a[pos] = a[i];
		a[i] = smallest;
		smallest = 32767;
	}

	printf("\nThe sorted array is: \n");
	for(i = 0; i < n; i++)
		printf("%d, ", a[i]);

	getch();
	return 0;
}