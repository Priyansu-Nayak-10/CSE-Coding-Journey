// copy the first array into second array 
#include<stdio.h>
#include<stdlib.h>
#define a_size 5
#define randmax 100
int main(){
int a[a_size], i,sum,b[a_size];
for(i=0; i< a_size; i++){
a[i]=rand()%randmax;
}
for(i=0;i<a_size;i++){
printf("a[%d] has value %d\n",i,a[i]);
}
for(i =0;i<a_size;i++){
b[i]=a[i];
}
for(i=0;i<a_size;i++){
printf("b[%d] has value %d\n",i,b[i]);
}
}
