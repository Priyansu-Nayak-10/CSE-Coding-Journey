#include<stdio.h>
#include<string.h>
struct planet{
char name[10];
double dia;
int moon;
};
struct planet getplanet(){
struct planet p;
strcpy(p.name,"Earth");
p.dia=4523.12;
p.moon=1;
return p;
}

void main(){
struct planet curr_planet;
curr_planet=getplanet();
printf("Name: %s\nDiameter:%.2lf\nMoon:%d\n",curr_planet.name,curr_planet.dia,curr_planet.moon);

}
