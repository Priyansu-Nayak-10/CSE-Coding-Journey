#include<stdio.h>
int main(){

char class;
printf("Enter ship serial number : ");
scanf("%c",&class);
printf("ship class is %c: ",class);
switch(class){
     case 'B':
     case 'b':
     printf("battleship \n"); break;
     case 'c':
     case 'C':
     printf("Cruiser\n");break;
     case 'd':
     case 'D':
     printf("Destroyer\n");break;
     case 'f':
     case 'F':
     printf("frigate\n");break;
     default:
     printf("unknown\n");
}
return 0;

}
