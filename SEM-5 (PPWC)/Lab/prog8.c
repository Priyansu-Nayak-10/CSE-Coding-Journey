#include<stdio.h>
int main (){
int sp, profit, totalcp;
float cp;
 printf("Enter the selling price of 15 item : ");
 scanf("%d",&sp);
 
 printf("Enter the cost price of 15 item : ");
 scanf("%d",&profit);
  totalcp=sp-profit;
  
  cp=totalcp/(float)15;
  
  printf("cost price of one item %f\n",cp);
  return 0;
 


}
