// print the random number 
#include<stdio.h>
#include<stdlib.h>
#define a_size 5
#define randmax 100
int main(){
int arr[a_size], i,sum;
for(i=0; i< a_size; i++)
arr[i]=rand()%randmax;

for(i=0;i<a_size;i++)
printf("arr[%d] has value %d\n",i,arr[i]);

}
