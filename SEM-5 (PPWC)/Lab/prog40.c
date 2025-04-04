#include<stdio.h>
int main(){
int i,j;
int n=6;
for(i=0;i<6;i++)
{
for(j=0;j<=i;j++)
{
printf("%d",j);
}
printf("\n");
}
for(i=n-1;i>0;i--){
for(j=0;j<i;j++){
printf("%d",j);
}
printf("\n");
}

}
