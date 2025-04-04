#include<stdio.h>
#define PI 3.14
int main(){
  char ch;
  
  printf("Enter the character C or S :");
  scanf("%c",&ch);
  
  if(ch=='c'|| ch=='C'){
       int rd;
       printf("Enter the radius : ");
       scanf("%d",&rd);
       int area=PI*rd*rd;
       printf("the area of a circle :  %d\n",area);
  
  }else if(ch=='s'||ch=='S'){
       int sq;
       printf("Enter the side : ");
       scanf("%d",&sq);
       int area1=sq*sq;
       printf("the area of a square :  %d\n",area1);
  }
  else{
  printf("enter a valid character");
  }
  return 0;
}
