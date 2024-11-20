#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define MAX 5

typedef struct {
    int a[MAX];
    int rear;
    int front;
} Q;

void display(Q* q){
    for(int i = 0; i < MAX; i++){
        printf("%d ", q->a[i]);
    }
    printf("\nf:%d r:%d\n", q->front, q->rear);
}


void enq(Q* q, int x){
    if((q->front == 0 && q->rear == MAX - 1) || (q->rear + 1 == q->front)){
        printf("Q Full\n"); return;
    }
    if(q->front == -1){
        q->front = 0;
    }
    q->rear = (q->rear + 1) % MAX;
    q->a[q->rear] = x;
    display(q);
}

int deq(Q* q){
    if(q->front == -1){printf("Q Empty\n"); return -99;}
    int temp = q->a[q->front];
    q->a[q->front] = 0;
    if(q->front == q->rear){
        q->front = q->rear = -1;
    } else {
        q->front = q->front + 1 % MAX;
    }
    display(q);
    return temp;
}


void main(){
    Q* q = (Q*) malloc(sizeof(Q));
    q->front = q->rear = -1;
    enq(q, 10);
    enq(q, 20);
    enq(q, 30);
    enq(q, 40);
    enq(q, 50);
    deq(q);
    deq(q);
    enq(q, 60);
    enq(q, 70);
    enq(q, 80);
}

// 10 0 0 0 0 
// f:0 r:0
// 10 20 0 0 0 
// f:0 r:1
// 10 20 30 0 0 
// f:0 r:2
// 10 20 30 40 0 
// f:0 r:3
// 10 20 30 40 50 
// f:0 r:4
// 0 20 30 40 50 
// f:1 r:4
// 0 0 30 40 50 
// f:2 r:4
// 60 0 30 40 50 
// f:2 r:0
// 60 70 30 40 50 
// f:2 r:1
// Q Full