#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct {
  int arr[MAX];
  int size;
} Heap;

void swap(int *a, int *b){
  int temp = *a;
  *a = *b;
  *b = temp;
}

void heapTopDown(Heap* h, int a){
  h->arr[h->size] = a;
  int curr = h->size++;
  while(curr > 0){
    int par = (curr - 1) / 2;
    if(h->arr[curr] < h->arr[par]){
      swap(&h->arr[curr], &h->arr[par]);
      curr = par;
    } else {
      break;
    }
  }
}

void print(Heap *h){
  for(int i = 0; i < h->size; i++){
    printf("%d ", h->arr[i]);
  }
  printf("\n");

}

int main(){
  int arr[] = {20, 15, 30, 5, 10, 12};
  int n = sizeof(arr) / sizeof(arr[0]);
  Heap* h = (Heap*) malloc(sizeof(Heap));

  for(int i = 0; i < n; i++){
    heapTopDown(h, arr[i]);
    printf("Heap after inserting %d: ", arr[i]);
    print(h);
  }

  return 0;
}
