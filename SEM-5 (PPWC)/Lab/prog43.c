// program to assign the square of index as array element

#include<stdio.h>
int main(){
int i,n;
int a[100];
printf("The length of the array: ");
scanf("%d",&n);
for(i=0;i<=n;i++){
a[i]=i*i;
}
for(i=0;i<=n;i++){
printf("arr[%d] = %d\n",i, a[i]);

}
return 0;

}
