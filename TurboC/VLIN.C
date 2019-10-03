
	{
		if(a[i] == t)
		{
			pos = i;
			printf("Target found at position = %d. \nPress c if you want to continue searching for that element:", pos+1);
			scanf(" %c", &c);
			if(c=='c' || c=='C')
				continue;
			else	break;
		}
		pos = -2;
	}
	if(pos == -1)
		printf("Item not found.");
	if(pos == -2)
		printf("No more instances of target element was found. ");
	getch();
	return 0;
}
