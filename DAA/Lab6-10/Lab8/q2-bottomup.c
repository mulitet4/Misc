#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int comparisons;
    int swaps;
} OperationCount;

void swap(int* a, int* b, OperationCount* opCount) {
    int temp = *a;
    *a = *b;
    *b = temp;
    opCount->swaps++; 
}

void heapify(int arr[], int n, int i, OperationCount* opCount) {
    int largest = i; 
    int left = 2 * i + 1; 
    int right = 2 * i + 2; 

    if (left < n) {
        opCount->comparisons++;
        if (arr[left] > arr[largest]) {
            largest = left;
        }
    }

    if (right < n) {
        opCount->comparisons++; 
        if (arr[right] > arr[largest]) {
            largest = right;
        }
    }

    if (largest != i) {
        swap(&arr[i], &arr[largest], opCount); 
        heapify(arr, n, largest, opCount); 
    }
}

void buildMaxHeap(int arr[], int n, OperationCount* opCount) {
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i, opCount);
    }
}

void heapSort(int arr[], int n, OperationCount* opCount) {
    buildMaxHeap(arr, n, opCount); 

    for (int i = n - 1; i > 0; i--) {
        swap(&arr[0], &arr[i], opCount); 
        heapify(arr, i, 0, opCount); 
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    printf("Enter elements, -1 to stop");
    int arr[100];
    int n = -1;
    while(1){
	    int inp; scanf("%d", &inp);
	    if(inp == -1) break;
	    arr[++n] = inp;
    }
    printf("Unsorted array:\n");
    printArray(arr, n+1);

    OperationCount opCount = {0, 0}; 

    heapSort(arr, n+1, &opCount);

    printf("Sorted array:\n");
    printArray(arr, n+1);

    printf("Total comparisons: %d\n", opCount.comparisons);
    printf("Total swaps: %d\n", opCount.swaps);

    return 0;
}
