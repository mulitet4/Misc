#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define MAX 5

typedef struct {
    int a[MAX];
    int pr[MAX];
    int front;
    int rear;
} Q;

void enq(Q* q, int data, int pr){
    int i = q->rear;
    if(q->rear == MAX - 1){printf("Q Full\n"); return;}
    if(q->front == -1){q->front = 0;}
    for(i = q->rear; i >= q->front; i--){
        if(q->pr[i] > pr){
            q->pr[i+1] = q->pr[i];
            q->a[i+1] = q->a[i];
        } else {
            break;
        }
    }
    q->a[i+1] = data;
    q->pr[i+1] = pr;
    q->rear++;
}

int deq(Q* q){
    if(q->front == -1){printf("Q Empty\n"); return -99;}
    int temp = q->a[q->front];
    q->a[q->front] = 0;
    q->pr[q->front] = 0;
    if(q->front == q->rear){
        q->front = q->rear = -1;
    } else {
        q->front++;
    }
    return temp;
}

void display(Q* q){
    for(int i = 0; i < MAX; i++){
        printf("(%d, %d), ",q->a[i], q->pr[i]);
    }
    printf("\n");
}

void main(){
    Q* q = (Q*) malloc(sizeof(Q));
    q->front = q->rear = -1;
    enq(q, 10, 3);
    display(q);
    enq(q, 20, 2);
    display(q);
    enq(q, 30, 5);
    display(q);
}

// > : ascending
// < : descending
// (10, 3), (0, 0), (0, 0), (0, 0), (0, 0), 
// (20, 2), (10, 3), (0, 0), (0, 0), (0, 0), 
// (20, 2), (10, 3), (30, 5), (0, 0), (0, 0), 