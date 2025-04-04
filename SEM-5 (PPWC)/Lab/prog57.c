#include<stdio.h>
void sum_avg(double n1, double n2, double n3, double *sum, double *avg);
int main(void)
{
double n1,n2,n3,sum,avg;
printf("Enter the values for n1,n2,n3: \n");
scanf("%lf%lf%lf", &n1,&n2,&n3);
sum_avg(n1,n2,n3, &sum, &avg);
printf("Sum= %.2lf avg = %.2lf\n",sum, avg);
}
void sum_avg(double n1, double n2, double n3, double *sum, double *avg){
*sum=n1+n2+n3;
*avg=*sum/3;

}
