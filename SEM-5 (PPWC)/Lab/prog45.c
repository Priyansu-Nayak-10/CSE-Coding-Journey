// program to take element from standard input as array element

#include<stdio.h>
int main(){
int i,n,sum=0;
int a[100];
printf("The length of the array: ");
scanf("%d",&n);
printf("Enter the array element ");
for(i=0;i<n;i++){
scanf("%d",&a[i]);
}
for(i=0;i<n;i++){
sum=sum+a[i];

}
printf("sum of the elements %d\n",sum); 
return 0;

}
