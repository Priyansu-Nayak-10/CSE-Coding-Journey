#include<stdio.h>
#include<string.h>
int main(){
char s[]="Jan, 30, 1996";
char res1[5];
char res2[5];
char res3[5];
strncpy(res1,s,3);
strncpy(res2,&s[5],2);
str cpy(res3,&s[9]);
printf("%s\n",res1);
printf("%s\n",res2);
printf("%s\n",res3);


}
