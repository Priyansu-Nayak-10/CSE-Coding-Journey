#include<stdio.h>
int main(){
int status=0, sum=0, num;
while(status !=1){
printf("Enter a number");
scanf("%d",&num);
sum+=num;
if(sum>=100){
status=1;
}
}
printf("sum =%d\n",sum);


}
