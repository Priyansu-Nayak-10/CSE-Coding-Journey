#include <stdio.h>

int main() {
    double max = 100;
    double s1, s2, s3;
    char name[50];
    
    for (int i = 0; i < 3; i++) {
        printf("Enter the name of student %d: ", i + 1);
        scanf("%s", name);
        
 
        printf("Enter the marks obtained in MATH: ");
        scanf("%lf", &s1);
        printf("Enter the marks obtained in Physics: ");
        scanf("%lf", &s2);
        printf("Enter the marks obtained in Chemistry: ");
        scanf("%lf", &s3);
        
        double Tot = s1 + s2 + s3 ;
        double avg = (Tot / 3);
        

        printf("The average mark  %s is: %.2lf\n", name, avg);
    }
    
    return 0;
}

