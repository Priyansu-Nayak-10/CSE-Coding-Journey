#include<stdio.h>
void sum(int a, int b);
int main(){
int x=2,y=3;
sum(x,y);
}
void sum(int a, int b){
int r;
r=a+b; 
printf("sum : %d\n",r);
}
