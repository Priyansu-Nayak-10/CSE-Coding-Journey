#include<stdio.h>
long long factorial(int n) {
    if (n < 0) return -1; 
    long long result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}
int is_prime(int n) {
    if (n <= 1) return 0; 
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0; 
    }
    return 1;
}
const char* odd_or_even(int n) {
    return (n % 2 == 0) ? "Even" : "Odd";
}
int main() {
    int choice, number;
    do {
        printf("\nMenu:\n");
        printf("1. Factorial of a number\n");
        printf("2. Check if a number is prime\n");
        printf("3. Check if a number is odd or even\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
       switch (choice) {
            case 1:
                printf("Enter a number to find its factorial: ");
                scanf("%d", &number);
                if (number < 0) {
                    printf("Factorial is not defined for negative numbers.\n");
                } else {
                    printf("Factorial of %d is %lld\n", number, factorial(number));
                }
                break;
            case 2:
                printf("Enter a number to check if it is prime: ");
                scanf("%d", &number);
                if (is_prime(number)) {
                    printf("%d is a prime number.\n", number);
                } else {
                    printf("%d is not a prime number.\n", number);
                }
                break;
            case 3:
                printf("Enter a number to check if it is odd or even: ");
                scanf("%d", &number);
                printf("%d is %s.\n", number, odd_or_even(number));
                break;
            case 4:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 4);
    return 0;
}

