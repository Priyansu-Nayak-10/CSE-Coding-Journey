#include<stdio.h>
int main(){

int i,n,max,min,ele;
printf("Enter total no of element : ");
scanf("%d",&ele);
printf("Enter first number : ");
scanf("%d",&n);
max=n;
min=n;
for(i=0;i<ele-1;i++)
{
 printf("Enter another number : ");
 scanf("%d",&n);
 if(n>max)
 max=n;
 if(n<min)
 min=n;

}
printf("max no : %d\n",max);
printf("min no : %d\n",min);





}
