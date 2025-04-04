#include <stdio.h>

void distinct(int arr[], int size, int res[], int *res_size) {
    int k = 0;  
    for (int i = 0; i < size; i++) {
        int found = 0;
        
        for (int j = 0; j < k; j++) {
            if (arr[i] == res[j]) {
                found = 1;
                break;
            }
        }
        
        if (!found) {
            res[k++] = arr[i];
        }
    }
    *res_size = k; 
}
int main() {
    int arr[] = {6, 7, 7, 3, 1, 5, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    int result[size]; 
    int result_size = 0; 
    distinct(arr, size, result, &result_size); 
    printf("Distinct array: ");
    for (int i = 0; i < result_size; i++) {
        printf("%d ", result[i]);
    }
    return 0;
}

