#include <stdio.h>
#include <stdlib.h>

int opcount = 0;
void pr(int a){
    printf("%d\n", a);
}
void swap(int* a, int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high){
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if(arr[j] < pivot){
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[high]);
    return i+1;
}

void quicksort(int arr[], int low, int high){
    if(low >= high) return;
    int part = partition(arr, low, high);
    quicksort(arr, low, part-1);
    quicksort(arr, part+1, high);
}

void main(){
    int arr[] = {13, 15, 99, 2, 3, 6, 9, 14, 55};
    int size = sizeof(arr)/sizeof(int);
    quicksort(arr, 0, size-1);
    for(int i = 0; i < size; i++){ printf("%d ", arr[i]);}
}