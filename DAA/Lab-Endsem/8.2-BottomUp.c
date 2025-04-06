#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

void swap(int *a, int *b){
  int temp = *a;
  *a = *b;
  *b = temp;
}

void heapify(int arr[], int n, int i){
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;
  if(left < n && arr[largest] < arr[left]) largest = left;
  if(right < n && arr[largest] < arr[right]) largest = right;
  if(largest != i){
    swap(&arr[i], &arr[largest]);
    heapify(arr, n, largest);
  }
}

void buildMaxHeap(int arr[], int n){
  for(int i = (n / 2) - 1; i >= 0; i--){
    heapify(arr, n, i);
  }
}

void heapSort(int arr[], int n){
  buildMaxHeap(arr, n);
  for(int i = n - 1; i >= 0; i--){
    swap(&arr[0], &arr[i]);
    heapify(arr, i, 0);
  }
}

void printArray(int arr[], int n){
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}


int main(){
  int arr[] = {12, 11, 13, 5, 6, 7};
  int n = sizeof(arr) / sizeof(arr[0]);
  heapSort(arr, n);
  printArray(arr, n);
}