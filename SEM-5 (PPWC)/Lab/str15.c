#include<stdio.h>
#include<string.h>
int ifexists(char u, char p[], int v, int q[])
{
int i;
for(i=0;i<v;i++){
if(p[i]==u){
q[i]++;
return (1);
}
}
if(i>v)return (0);
}
void main()
{
char str1[80], str2[80];
int n,i,x,count[80];
printf("Enter a string:");
scanf("%s",str1);
n=strlen(str1);
str2[0]=str1[0];
x=1;
for(i=1;i<n;i++)
{
if(ifexists(str1[1],str2,x))
{
printf("The first repetitive character in %s is %c",str1,str1[i]);
break;
}
else{
str2[x]=str1[i];
x++;
}
}
if(i==n)
printf("no repetitive character");
}
