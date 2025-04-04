#include<stdio.h>
struct planet_t{
char name[10];
double r_t, dia;
int moon;
};

void main(){
struct planet_t p[4];
int i;
printf("Enter planet name rotation diameter and no of moon\n");
for(i=0;i<4;i++){
scanf("%s %lf %lf %d",p[i].name,&p[i].r_t,&p[i].dia,&p[i].moon);
}
for(i=0;i<4;i++)
{
printf("name=%s\nrotation=%lf\nDiameter=%lf\nMoon=%d\n",p[i].name,p[i].r_t,p[i].dia,p[i].moon);
}

}
