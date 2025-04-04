// program to take element from standard input as array element

#include<stdio.h>
int main(){
int i,n;
int a[100];
printf("The length of the array: ");
scanf("%d",&n);
printf("Enter the array element ");
for(i=0;i<n;i++){
scanf("%d",&a[i]);
}
for(i=0;i<n;i++){
printf("arr[%d] = %d and address is %p\n",i,a[i],&a[i]); // to print the address 

}
return 0;

}
