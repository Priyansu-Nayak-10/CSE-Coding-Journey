#include<stdio.h>
int gcd(int p, int q);
void main()
{
int x,y,g;
printf("Enter two numbers:");
scanf("%d %d", &x, &y);
g=gcd(x,y);
printf("GCD of %d and %d is %d",x,y,g);
}
int gcd(int a, int b)
{
int m;
m=a%b;
if(m==0)
return (b);
else
gcd(b,m);
}
