#include<stdio.h>
int val=10;
int main(void)
{
 int val = 20;
 {
 	extern int val;
 	printf("Global variable val=%d\n",val);
 }
 printf("local variable val=%d\n",val);
 return 0;
 }
