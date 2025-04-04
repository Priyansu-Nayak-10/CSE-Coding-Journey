
#include <stdio.h>
#define ms 10
int main() {
    int arr[ms], n, i, j, count = 0;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    printf("Enter the elements of the array:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            if (arr[i] == arr[j]) {
                count++;
                break;
            }
        }
    }
   
    printf("Total number of duplicate elements: %d\n", count);
    return 0;
}

