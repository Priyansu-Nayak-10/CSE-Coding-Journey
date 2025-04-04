#include<stdio.h>
int main(){

char ca;
 printf("Enter the character : ");
 scanf("%c",&ca);
 
 if (ca >= 'a' && ca <= 'z') {
        printf("The character '%c' is a lowercase letter. \n", ca);
    } else if (ca >= 'A' && ca <= 'Z') {
        printf("The character '%c' is an uppercase letter.\n", ca);
    } else if (ca >= '0' && ca <= '9') {
        printf("The character '%c' is a digit.\n", ca);
    } else {
        printf("please enter a valid character.%c\n", ca);
    }
    return 0;

}
