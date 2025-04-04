#include<stdio.h>
int main(){

int s1,s2,s3,s4,s5;
int total=500;
int agg;
float per;
char a,b,c,d;
printf("Enter the name of the student: ");
scanf("%c%c%c%c",&a,&b,&c,&d);
printf("Enter the mark of math: ");
scanf("%d",&s1);
printf("Enter the mark of phy: ");
scanf("%d",&s2);
printf("Enter the mark of chem: ");
scanf("%d",&s3);
printf("Enter the mark of Bio: ");
scanf("%d",&s4);
printf("Enter the mark of eng: ");
scanf("%d",&s5);

agg=s1+s2+s3+s4+s5;

per=(agg/(float)500)*100;

printf("total aggregate mark: %d\n",agg);
printf("percentage  : %f%%\n",per);

}
