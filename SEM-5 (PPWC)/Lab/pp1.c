//user input
#include<stdio.h>
char pop(char stack[], int *top);
void push(char stack[], char item, int *top, int max);
#define max 20
int main(){
char stack[max];
int top =-1, i, j;

for(i=0;i<=top; i++){
printf("%c ", stack[i]);
}
printf("\n");

for(j=top;j> -1;j--){
printf("The value popped: %c\n", pop(stack, &top));
}
}
void push(char stack[], char item, int *top, int m){
if(*top<m-1){
++(*top);
stack[*top]=item;
}
}
char pop(char stack[], int *top){
char item;
if(*top>=0){
item = stack[*top];
--(top);
}
else{
printf("stack is empty");
}
return(item);
}
