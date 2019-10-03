#include<stdio.h>
#include<conio.h>

#define MAX 100

void M(int a[], int l, int m, int r)
{
	int i, j, k = 0;
	int n1 = m-l+1;
	int n2 = r - m;

	int L[MAX], R[MAX];

	for(i = 0; i< n1; i++)
		L[i] = a[l+i];
	for(j = 0; j< n2; j++)
		R[j] = a[m+1+j];

	i = 0; j = 0; k = l;

	while(i < n1 && j < n2)
	{
		if( L[i] <= R[i] )
		{
			a[k] = L[i];
			k++; i++;
		}
		else
		{
			a[k] = R[j];
			k++; j++;
		}
	}
	while(i < n1)
	{
		a[k] = L[i];
		k++; i++;
	}
	while(j < n2)
	{
		a[k] = R[j];
		k++; j++;
	}
}

void MS(int a[], int l, int r)
{
	int i;

	if(l < r)
	{
		int m = (l+r)/2;

		MS(a, l, m);
		MS(a, m + 1, r);
		M(a, l, m, r);

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

	MS(a, 0, n-1);

	printf("The sorted array is: ");
	for(i = 0; i < n; i++)
		printf("%d, ", a[i]);
	getch();
	return 0;
}