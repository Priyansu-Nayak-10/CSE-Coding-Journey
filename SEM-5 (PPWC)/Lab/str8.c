#include<stdio.h>
#include<string.h>
int main()
{
char str[]="hello-iter";
char *token = strtok(str,"-");
while (token !=NULL)
{
printf("%s\n",token);
token=strtok(NULL,"-");
}
}
