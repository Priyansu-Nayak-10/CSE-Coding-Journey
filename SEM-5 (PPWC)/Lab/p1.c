//program for circle
#include<stdio.h>
#define PI 3.1459

int main(){
    float area,radius, circumf ;
    float num_circ;
    printf("Enter the radius ");
    scanf("%f", &radius);
    area=PI*radius*radius;
    num_circ=2*PI*radius;
    printf("the area of circle is %f", area);
     printf("\nthe area of circle is %f", circumf);
    return 0;
    
}
