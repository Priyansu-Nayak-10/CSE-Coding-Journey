#include<stdio.h>
int main(void){
int sum =0,score, insta;
printf("Scores\n");
insta = scanf("%d", &score);

while(insta !=EOF){
printf("%5d\n",score);
sum+=score;

insta = scanf("%d",&score);
printf("Value returned %d", insta);
}
printf("\nSum ofexam scores is %d\n",sum);
return (0);
}
