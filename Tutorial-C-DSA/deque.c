#include <stdio.h>
#define MAX 5

typedef struct {
    int rear;
    int front;
    int a[MAX];
} DQ;

void insertFront(DQ* q, int elem){
    if(q->front == 0 && q->rear == MAX -1){
        printf("Q full");
        return;
    }
    if(q->front = -1 && q->rear == -1){
        q->rear = 0;
        q->front = 0;
    }
    else {
        for(int i = q->rear; i >= 0; i--){
            q->a[i+1] = q->a[i];
        }
        q->rear++;
    }
    q->a[q->front] = elem;
    printf("f:%d r:%d\n", q->front, q->rear);
}

void deleteRear(DQ* q, int elem){
    if(q->front == -1){
        printf("Q empty");
        return;
    }
    int temp = q->a[q->rear];
    if(q->front == q->rear){
        q->front = q->rear = -1;
        return;
    }
    q->rear--;
}

void display(DQ* q){
    for(int i = 0; i < MAX; i++){
        printf("%d\t", q->a[i]);
    }
    printf("\n");
}

void main(){
    DQ q;
    q.front = q.rear = -1;
    DQ* qp = &q;
    insertFront(qp, 3);
    insertFront(qp, 5);
    insertFront(qp, 6);
    display(qp);
}

// f:0 r:0
// f:0 r:1
// f:0 r:2
// 6	5	3	0	4198480