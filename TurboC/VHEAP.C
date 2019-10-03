#include<stdio.h>
#include<conio.h>

#define MAX 100

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void H(int a[], int n, int i)
{
	int largest = i;
	int l = 2 * i + 1;
	int r = 2 * i + 2;

	if(l < n && a[l] > a[largest])
		largest = l;
	if(r < n && a[r] > a[largest])
		largest = r;

	if(largest != i)
	{
		swap (&a[i], &a[largest]);
		H(a, n, largest);
	}
}

void HS(int a[], int n)
{
	int i;
	for(i = n/2 - 1; i>= 0; i--)
		H(a,n,i);
	printf("\n Building Max Heap: \n");
	for(i = 0; i < n; i++)
		printf("%d, ", a[i]);
	for(i = n-1; i>= 0; i--)
	{
		swap(&a[0], &a[i]);
		H(a, i, 0);
	}
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

	HS(a, n);

	printf("The sorted array is: ");
	for(i = 0; i < n; i++)
		printf("%d, ", a[i]);
	getch();
	return 0;
}