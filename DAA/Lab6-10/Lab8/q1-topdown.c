#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100

typedef struct {
    int arr[MAX_SIZE];
    int size;
} Heap;

int opCount = 0;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void heapifyDown(Heap *heap, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    opCount++;
    if (left < heap->size && heap->arr[left] > heap->arr[largest])
        largest = left;
    opCount++;
    if (right < heap->size && heap->arr[right] > heap->arr[largest])
        largest = right;
    opCount++;
    if (largest != i) {
        swap(&heap->arr[i], &heap->arr[largest]);
        heapifyDown(heap, largest);
    }
}

void buildHeap(Heap *heap) {
    for (int i = heap->size / 2 - 1; i >= 0; i--)
        heapifyDown(heap, i);
}

void main() {
    Heap* heap = (Heap*)malloc(sizeof(Heap));
    int n;
    printf("Enter the no. of integers: ");
    scanf("%d", &n);
    printf("Enter the integers: ");
    for (int i = 0; i < n; i++)
        scanf("%d", &heap->arr[i]);
    heap->size = n;
    buildHeap(heap);
    printf("Heap: ");
    for (int i = 0; i < heap->size; i++)
        printf("%d ", heap->arr[i]);
    printf("\nNumber of basic operations: %d\n", opCount);
}
