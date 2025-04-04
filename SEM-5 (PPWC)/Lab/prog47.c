// print the random number 
#include<stdio.h>
#include<stdlib.h>
int main(){
int arr[5], i,sum;

for(i=0; i< 5; i++)
arr[i]=rand()%100;

for(i=4;i>0;i--)
printf("arr[%d] has value %d\n",i,arr[i]);

}
