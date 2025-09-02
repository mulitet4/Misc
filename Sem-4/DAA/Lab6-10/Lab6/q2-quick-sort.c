#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high, int* opc) {
    int pivot = arr[high]; // Choose the last element as the pivot
    int i = (low - 1); // Index of the smaller element
    for (int j = low; j < high; j++) {
	(*opc)++;
	if (arr[j] <= pivot) {
		i++; // Increment index of smaller element
		swap(&arr[i], &arr[j]); // Swap elements
	}
    }
    swap(&arr[i + 1], &arr[high]); // Place the pivot in the correct position
    return (i + 1); // Return the index of the pivot
}

void quickSort(int a[], int l, int r, int *opc){
	if(l >= r) return;
	int part_ind = partition(a, l, r, opc);
       	quickSort(a, l, part_ind - 1, opc);
	quickSort(a, part_ind + 1, r, opc);
}

void main(){
	int a[100], len = -1, inp, opcount = 0, *opc = &opcount;
	printf("Enter elements, -1 to exit: \n");
	while(1){
		scanf("%d", &inp);
		if(inp == -1) break;
		a[++len] = inp;
	}
	quickSort(a, 0, len, opc);
	for(int i = 0; i <= len; i++){
		printf("%d ", a[i]);
	}
	printf("Opcount: %d", opcount);
}
