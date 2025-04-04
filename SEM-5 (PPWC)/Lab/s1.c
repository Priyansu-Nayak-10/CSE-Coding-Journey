#include<stdio.h>
struct book_data{
int page;
char name;
};
int main(){
struct book_data b1={200,'A'},b2;
printf("Enter the value of b2\n");
scanf("%d",&b2.page);
scanf(" %c",&b2.name);
printf("the elements page: %d name: %c",b2.page,b2.name);
}
