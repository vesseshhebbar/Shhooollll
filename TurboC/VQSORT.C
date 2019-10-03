#include<stdio.h>
#include<conio.h>

#define MAX 100

void Q(int a[], int l, int h)
{
	if(l<h)
	{
		int j;
		j = part(a, l,h);
		Q(a, l, j);
		Q(a, j+1, h);
	}
}

int part(int a[], int l, int h)
{
	int pivot = a[l], i, j, tmp;
	i = l;
	j = h;

	while(i<j)
	{
		do
		{
			i++;
		}while(a[i] <= pivot);
		do
		{
			j--;
		}while(a[j] > pivot);
		if(i < j)
		{
			tmp = a[i];
			a[i] = a[j];
			a[j] = tmp;
		}
	}
	tmp = a[l];
	a[l] = a[j];
	a[j] = tmp;

	return j;
}


int main()
{
	int a[MAX], n, i, j, k;
	clrscr();

	printf("Enter the size of array (max %d): ", MAX);
		scanf("%d", &n);
	printf("Enter the array: ");
	for(i = 0; i < n; i++)
		scanf("%d", &a[i]);

	Q(a, 0, n);

	printf("The sorted array is: ");
	for(i = 0; i < n; i++)
		printf("%d, ", a[i]);
	getch();
	return 0;
}