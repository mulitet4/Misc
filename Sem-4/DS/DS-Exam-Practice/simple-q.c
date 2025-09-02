#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define MAX 5

typedef struct {
    int a[MAX];
    int front;
    int rear;
} Q;

void enq(Q* q, int data){
    if(q->rear == MAX - 1){
        printf("Q Full\n"); return;
    }
    if(q->front == -1 && q->rear == -1) q->front = 0;
    q->a[++q->rear] = data;
}

int deq(Q* q){
    if(q->front == -1){
        printf("Q Empty\n"); return -99;
    }
    int temp = q->a[q->front];
    if(q->front == q->rear){
        q->front = q->rear = -1;
    } else {
        q->front++;
    }
    return temp;
}

void display(Q* q){
    for(int i = q->front; i <= q->rear; i++){
        printf("%d ", q->a[i]);
    }
    printf("\n");
}

void main(){
    Q* q = (Q*) malloc(sizeof(Q));
    q->front = q->rear = -1;
    enq(q, 10);
    enq(q, 20);
    enq(q, 30);
    enq(q, 40);
    enq(q, 50);
    enq(q, 60);
    display(q);
    printf("%d f:%d r:%d\n", deq(q), q->front, q->rear);
    printf("%d f:%d r:%d\n", deq(q), q->front, q->rear);
    printf("%d f:%d r:%d\n", deq(q), q->front, q->rear);
    printf("%d f:%d r:%d\n", deq(q), q->front, q->rear);
    printf("%d f:%d r:%d\n", deq(q), q->front, q->rear);
    printf("%d f:%d r:%d\n", deq(q), q->front, q->rear);
    enq(q, 50);
    enq(q, 60);
    display(q);
}