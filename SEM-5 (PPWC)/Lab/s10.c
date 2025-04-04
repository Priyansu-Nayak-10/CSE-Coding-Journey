#include<stdio.h>
struct planet{
char name[10];
double dia;
int moon;
double r_t;
};
void scan_plan(struct planet *p1);
void main(){
struct planet p1;
scan_plan(&p1);
printf("name=%s diameter=%lf moon=%d rotation=%lf\n",\]p1.name,p1.dia,p1.moon,p1.r_t);
}
void scan_plan(struct planet *p1){
scanf("%s%lf%d%lf",p1->name,&p1->dia,&p1->moon,&p1->r_t);
}
