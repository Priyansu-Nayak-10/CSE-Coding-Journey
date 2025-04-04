#include<stdio.h>
void main(){

int p[max];
int n,i,k,j;

printf("%d", &n);
printf("Enter %d elements of array\n",n);
for(i=0;i<=n-1;i++){
scanf("%d",&p[i]);
printf("\n The array is : \n");
for(i=0;i<n-1;i++)
printf("%d\n", p[i]);
printf("\n Enter position where to insert: ");
scanf("%d",&k);
k--;

for(j=n-1;j>=k;j--)
p[j+1]=p[j];
printf("\n Enter the value to insert.");
scanf("%d",&p[k]);
printf("\nArray after insertion of element : \n");
for(i=0;i<=n;i++)
printf("%d\n",p[i]);
}
}
