#include<stdio.h>
void funarr(int arr[], int n){
for(int i=0;i<n;i++)
{
printf(" %d", arr[i]);
}
printf("\n");
}
int main(void)
{
int arr[]={3,5,6,7};
int n,i;
n=sizeof(arr)/sizeof(arr[0]);
funarr(arr,n);
}

