#include<stdio.h>
#include<conio.h>

int main()
{
	int n=1, t, a[10], i, b,m,e;
	clrscr();
	printf("Enter the number of elements: ");
	scanf("%d", &n);
	printf("Enter the values of sorted array: ");
	for(i = 0; i < n; i++)
	scanf("%d", &a[i]);
	printf("Enter the target element to search for: ");
	scanf("%d", &t);

	b = 0, e = n-1, m = ( (b+e)/2);

	while (b < e)
	{       if(a[m] == t)
		{
			printf("Element found at position %d", m+1);
			getch();
			return 0;
		}
		else if(t < a[m])
		{
			e = m;
			m = (b+e)/2;
		}
		else if(t > a[m])
		{
			b = m;
			m = (b+e)/2;
		}
	}
	printf("Element not found.");

	getch();
	return 0;
}