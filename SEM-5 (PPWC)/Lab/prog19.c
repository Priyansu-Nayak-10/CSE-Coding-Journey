#include <stdio.h>
#include<time.h>
int main(){
clock_t s,e;
double exetime1, exetime2;
int i;
s=clock();
for (i=0;i<100000000;i++){
auto int x=1;
x++;
}
e=clock();
exetime1=((double)(e-s))/CLOCKS_PER_SEC;
printf("Time taken is %f\n",exetime1);

s=clock();
for (i=0;i<100000000;i++){
register int x=1;
x++;
}
e=clock();
exetime1=((double)(e-s))/CLOCKS_PER_SEC;
printf("Time taken is %f\n",exetime1);
}
