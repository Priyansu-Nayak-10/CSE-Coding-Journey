#include<stdio.h>
int main(){
int wd;
printf("enter the amount");
scanf("%d",&wd);
int v1=wd/100;
int v2=wd%100;
int v3=v2/50;
int v4=v2%50;
int v5=v4/10;
int v6=v4%10;
printf("100 = %d\n",v1);
printf("50 = %d\n",v3);
printf("10 = %d\n",v5);


}
