#include<stdio.h>
struct book{
int page;
char name;
};
int main(){
struct book b1;
printf("Enter the contents page and name: ");
scanf("%d %c",&b1.page, &b1.name);
printf("Page:%d , Name:%c \n",b1.page, b1.name);
}
