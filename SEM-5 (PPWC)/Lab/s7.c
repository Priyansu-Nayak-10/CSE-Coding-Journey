#include<stdio.h>
struct book{
int page;
char name;
};
int main(){
struct book b1={34, 'A'},b2;
b2=b1;
printf("The data of b2\n");
printf("page:%d name:%c\n",b2.page,b2.name);
}

