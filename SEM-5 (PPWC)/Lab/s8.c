#include<stdio.h>
struct bank{
int acc_no;
char name[15];
double bal;
};
void main(){
struct bank b[4];
int i;
for(i=0;i<4;i++){
scanf("%d%s%lf",&b[i].acc_no,b[i].name,&b[i].bal);
}
for(i=0;i<4;i++)
{
printf("Account_no:%d name:%s balance:%.2lf",b[i].acc_no,b[i].name,b[i].bal);
}
}
