#include<stdio.h>
int main(){

int n1;
printf("Enter the number btw 1-4: ");
scanf("%d",&n1);

switch(n1){
 case 1:
 printf("Odd or even \n");
 int n2;
 printf("Enter a number : ");
 scanf("%d",&n2);
 if(n2%2==0){
 printf("the number is even\n");
 }else{
 printf("the number is odd \n");
 }
 break;
 case 3:
 printf("Exit");
 break;
 default:
 printf("Enter a valid number\n");
}
return 0;

}
