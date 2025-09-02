#include<stdio.h>
#include<stdlib.h>
#define MAX 3

typedef struct {
    int rear;
    int front;
    int a[MAX];
} CQ;

void enq(CQ* q, int elem){
    if(q->rear+1 == q->front || (q->front == 0 && q->rear == MAX-1)){
        printf("Q full\n");
        return;
    }
    if(q->rear == -1 && q->front == -1){
        q->front = 0;
    }
    q->rear = (q->rear + 1) % MAX;
    q->a[q->rear] = elem;
    printf("front: %d, rear: %d\n", q->front, q->rear);
}

int deq(CQ*q){
    if(q->rear == q->front){
        printf("Q Empty\n");
        return -99;
    }
    int temp = q->a[q->front];
    q->a[q->front] = 0;
    q->front = (q->front + 1) % MAX;
    if(q->front == q->rear){
        q->a[q->front] = 0;
        q->front = q->rear = -1;
    }
    printf("front: %d, rear: %d\n", q->front, q->rear);
    return temp;
}

void display(CQ* q){
    for(int i = 0; i < MAX; i++){
        printf("%d\t", q->a[i]);
    }
    printf("\n");
}

void main(){
    CQ q;
    q.front = q.rear = -1;
    for(int i = 0; i < MAX; i++){
        q.a[i] = 0;
    }
    CQ* qp = &q;
    enq(qp, 3);
    display(qp);
    
    enq(qp, 3);
    display(qp);

    enq(qp, 3);
    display(qp);
    
    deq(qp);
    display(qp);
    
    enq(qp, 3);
    display(qp);
    
    deq(qp);
    display(qp);
}


// front: 0, rear: 0
// 3	0	0	
// front: 0, rear: 1
// 3	3	0	
// front: 0, rear: 2
// 3	3	3	
// front: 1, rear: 2
// 0	3	3	
// front: 1, rear: 0
// 3	3	3	
// front: 2, rear: 0
// 3	0	3