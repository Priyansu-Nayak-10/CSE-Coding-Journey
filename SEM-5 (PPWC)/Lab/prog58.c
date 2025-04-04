#include<stdio.h>
#include<math.h>
void separate(double num,char *signp, int *wholep, double *fracp )
{
double magnitude;
if(num<0)
  *signp='-';
else *signp='+';
  magnitude = fabs(num);
*wholep=floor(magnitude);
*fracp=magnitude-*wholep;
}
int main(void){
double value;
char sign;
int whl;
double fr;
printf("Enter the value to analyze: ");
scanf("%lf",&value);
separate(value, &sign,&whl,&fr);
printf("Parts of %.4f\n sign: %c\n", value,sign);
printf("whole number magnitude: %d\n",whl);
printf("fractional part: %.4lf\n",fr);
return (0);
}



