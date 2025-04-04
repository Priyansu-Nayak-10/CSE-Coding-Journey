
#include<stdio.h>
int main(){
   int num;
   printf("Enter the number of employees :");
   scanf("%d",&num);
   int e;
   int payr=0;
   for(e=0;e<num;e++){ 
   printf("employee : %d\n",e);
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
   printf("Total payroll is $ %d\n",payr);
   return 0;

}
