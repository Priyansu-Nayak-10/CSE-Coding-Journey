#include<stdio.h>
int main(){
int marks;
printf("Enter the number:-");
scanf("%d",&marks);
if(marks>90){
printf("Grade 'O'");
}
else if (marks>80){
printf("Grade 'A'");
}
else if (marks>70){
printf("Grade 'B'");
}
else if (marks>60){
printf("Grade 'C'");
}
else if (marks>50){
printf("Grade 'D'");
}
else{
printf("Grade 'E'");

}
return 0;
}
