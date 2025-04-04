/* A program that computes and display the gross pasy for seven employees
input: hours worked, rate, pay
pay=hours*rate*/

#include<stdio.h>
int main(){
   int num;
   printf("Enter the number of employees :");
   scanf("%d",&num);
   int e=1;
   int payr=0;
   while(e<num){ 
   printf("employee : %d\n",e);
   e++;
   int hr,rate;
   printf("hours worked  :");
   scanf("%d",&hr);
   printf("Rate : ");
   scanf("%d",&rate);
   int pay=hr*rate;
   printf("pay : %d\n",pay);
   
   payr+=pay;
   
}
   printf("All employee processed");
   printf("Total payroll is $ %d",payr);
   return 0;

}
