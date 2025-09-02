#include <stdio.h>
#include <stdlib.h>

void merge(int *arr, int l, int mid, int r){
  int lsize = mid - l + 1;
  int rsize = r - mid;
  int ltemparr[lsize];
  int rtemparr[rsize];
  for(int i = 0; i < lsize; i++){
    ltemparr[i] = arr[l + i];
  }
  for(int i = 0; i < rsize; i++){
    rtemparr[i] = arr[mid + 1 + i];
  }
  int i = 0, j = 0, k = l;
  while( i < lsize && j < rsize ){
    if(ltemparr[i] < rtemparr[j]){
      arr[k++] = ltemparr[i++];
    } else {
      arr[k++] = rtemparr[j++];
    }
  }
  while(i < lsize){
    arr[k++] = ltemparr[i++];
  }
  while(j < rsize){
    arr[k++] = rtemparr[j++];
  }
}

void mergeSort(int* arr, int low, int high){
  if(low >= high) return;
  int mid = ( low + high  )/ 2;
  mergeSort(arr, low, mid);
  mergeSort(arr, mid+1, high);
  merge(arr, low, mid, high);
}

void main(){
  int array[] = {9, 4, 5, 1, 99, 3, 35, 34, 45};
  int size = sizeof(array)/sizeof(int);
  mergeSort(array, 0, size - 1);
  for (int i = 0; i < size; i++) { printf("%d ", array[i]); }
}