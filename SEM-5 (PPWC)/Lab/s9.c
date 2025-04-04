#include<stdio.h>
struct book{
int pgno;
char name[10];
};
void fun_print(struct book b1);
int main(){
struct book b1={100,"Math"};
fun_print(b1);
}
void fun_print(struct book b1){
printf("Page:%d Name:%s\n",b1.pgno,b1.name);
}
