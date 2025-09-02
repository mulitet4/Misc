#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b){
  int temp = *a;
  *a = *b;
  *b = temp;
}

int partition(int* arr, int l, int r){
  int pivot = arr[r];
  int i = l - 1;
  for(int j = l; j < r; j++){
    if(arr[j] < pivot){
      i++;
      swap(&arr[i], &arr[j]);
    }
  }
  swap(&arr[i+1], &arr[r]);
  return i+1;
}

void quickSort(int *arr, int l, int r){
  if(l >= r) return;
  int p = partition(arr, l, r);
  quickSort(arr, l, p-1);
  quickSort(arr, p+1, r);
}

void main(){
  int arr[] = {2, 6, 1, 9, 0, 5, 33, 14};
  int n = sizeof(arr) / sizeof(int);
  quickSort(arr, 0, n-1);
  for(int i = 0; i < n; i++) {printf("%d ", arr[i]);}
}