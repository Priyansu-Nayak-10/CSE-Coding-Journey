#include<stdio.h>
#include<string.h>
int main(){
char s1[30]="Hello";
char s2[10];
strncat(s2, "and more", 7);
printf("%s\n",s2);
}
