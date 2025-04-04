#include<stdio.h>
#include<string.h>
int main()
{
char str[]="hello-iter";
char *token = strtok(str,"-");
int c=0;
while (token !=NULL)
{
c++;
printf("%s\n",token);
token=strtok(NULL,"-");
}
printf("%d\n",c);
}
