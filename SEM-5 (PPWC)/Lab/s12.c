#include<stdio.h>
#include<stdlib.h>
int main(){
int i,n=100;
char *name;
name=(char*)malloc(n*sizeof(char));
printf("Enter your name:");
scanf("%s",name);
printf("Your name is =%s\n",name);
free(name);
return 0;
}
