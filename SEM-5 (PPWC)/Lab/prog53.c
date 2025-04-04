#include<stdio.h>
int main()
{
	int arr1[]={1,2,3};
	int arr2[]={3,2,1};
	int i,j, flag, x, k=0;
	int result[100];
	printf("common elements are : ");

	for(i=0; i < sizeof(arr1) / 4;i++)
	{
	for(j=0; j < sizeof(arr2) / 4;j++)
	{
	if(arr1[i]==arr2[j])
	{
	flag=0;
	for(x=0;x<k;x++)
	{
	if(result[x]==arr1[i])
	{
	flag++;
	}
	}
	if(flag==0)
	{
	result[k]=arr1[i];
	printf("%d",result[k]);
	k++;
	}
	}
	}
	}
	printf("\n");

}
