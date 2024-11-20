#include <stdio.h>
#include <stdlib.h>
#define MAX 3

typedef struct node {
    int a[MAX];
    int front;
    int rear;
} Q;

void enq(Q* q, int elem){
    if(q->rear == MAX - 1){
        printf("Q full"); return;
    }
    if(q->rear == -1 && q->front == -1){
        q->front = 0;
    }
    q->a[++q->rear] = elem;
}

int deq(Q* q){
    if(q->front == q->rear){
        printf("Q Empty"); return -99;
    }
    int temp = q->a[q->front++];
    if(q->front == q->rear){
        q->front = q->rear = -1;
    }
    return temp;
}

void display(Q* q){
    for(int i = q->front; i <= q->rear; i++){
        printf("%d ", q->a[i]);
    }
}

void main(){
    Q* q = (Q*) malloc(sizeof(Q));
    q->front = q->rear = -1;
    enq(q, 10);
    enq(q, 20);
    enq(q, 30);
    printf("%d\n", deq(q));
    display(q);
}


// 10
// 20 30 