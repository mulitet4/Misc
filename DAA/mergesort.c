#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int low, int high, int mid){
  int lsize = mid - low + 1;
  int rsize = high - mid;
  int ltemparr[lsize];
  int rtemparr[rsize];
  for(int i = 0; i < lsize; i++){
    ltemparr[i] = arr[low + i];
  }
  for(int i = 0; i < rsize; i++){
    rtemparr[i] = arr[mid + 1 + i];
  }
  int i = 0, j = 0, k = low;
  while(i < lsize && j < rsize){
    if(ltemparr[i] < rtemparr[j]){
      arr[k++] = ltemparr[i++]; 
    } else {
      arr[k++] = rtemparr[j++];
    }
  }
  while(i < lsize){ arr[k++] = ltemparr[i++]; }
  while(j < rsize){ arr[k++] = rtemparr[j++]; }
}

void mergesort(int arr[], int low, int high){
  if(low >= high) return;
  int mid = low + (high - low) / 2;
  mergesort(arr, low, mid);
  mergesort(arr, mid + 1, high);
  merge(arr, low, high, mid);
}

void main(){
  int array[] = {9, 4, 5, 1, 99, 3, 35, 34, 45};
  int size = sizeof(array)/sizeof(int);
  mergesort(array, 0, size - 1);
  for (int i = 0; i < size; i++) { printf("%d ", array[i]); }
}