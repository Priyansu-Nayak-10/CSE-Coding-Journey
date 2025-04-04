#include<stdio.h>
#include<string.h>
int main(){
char dest[20];
char src[]="GOOD MORNING";
char dest1[10];
strncpy(dest1,src,2);
dest1[2]='\0';
strcpy(dest,src);

printf("%s\n",dest);
printf("%s\n",dest1);

}
