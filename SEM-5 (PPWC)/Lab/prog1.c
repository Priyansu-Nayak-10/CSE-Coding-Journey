//prefix and postfix
#include<stdio.h>
int main(){
int x,y,z;
printf("enter the value of x : ");
scanf("%d",&x);
z=++x;
printf("prefix of x : %d \n ",z);

printf("enter the value of y : ");
scanf("%d",&y);
z=y++;
printf("postfix of y : %d \n",z);
return 0;
}
