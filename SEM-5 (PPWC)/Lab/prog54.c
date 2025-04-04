#include<stdio.h>
int sum();
int main(){
int r=sum();
printf("sum : %d\n",r);
return 0;
}
int sum(){
int a=2,b=4,r;
r=a+b; 
return(r);
}

/*
#include<stdio.h>
void sum();
int main(){
sum();

return 0;
}
void sum(){
int a=2,b=4,r;
r=a+b; 
printf("sum : %d\n",r);

}
*/
