#include<stdio.h>
int main(){

char lif;
printf("Enter the U for unmarried and m for married : ");
scanf("%c",&lif);


if(lif=='m'||lif=='M'){
 printf("The driver is married\n  ");
 }else if(lif=='u'||lif=='U'){ 
  char g; 
  printf("Enter M of male and F for female : \n");
  scanf(" %c",&g);
  if(g=='M'||g=='m'){
  int age;
   printf("Enter the age : \n");
   scanf("%d",&age);
   if(age>30){
   printf("the driver is unmarried , male and above 30 years \n");
   }else{
   printf("the driver age is below 30");
   }
  }else if(g=='F'||g=='f'){
  int age;
   printf("Enter the age : \n");
   scanf("%d",&age);
   if(age>25){
   printf("the driver is unmarried , female and above 25 years \n");
   }else{
   printf("the driver age is below 25\n");
   }
  }
  }else{
  printf("enter the valid character\n");
  }
return 0;

}
