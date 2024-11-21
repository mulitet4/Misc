#include <stdio.h>
#include <string.h>
#define MAX 5

typedef struct {
    int rear;
    int front;
    int a[MAX];
} Q;

void enq(Q* q, int elem){
    if(q->rear == MAX-1){
        printf("Q Full\n");
        return;
    }
    if(q->rear == -1 && q->front == -1){
        q->front = 0;
    }
    q->a[++q->rear] = elem;
}

int deq(Q* q){
    if(q->front == q->rear){
        printf("Q empty\n");
        return -99;
    }
    int temp = q->a[q->front++];
    if(q->front == q->rear){
        q->front = q->rear = -1;
    }
    return temp;
}

void display(Q* q){
    for(int i = q->front; i <= q->rear; i++){
        printf("%d\t", q->a[i]);
    }
    printf("\n");
}

int main() {
    Q q;
    q.front = q.rear = -1;
    Q* qp = &q;
    enq(qp, 5);
    display(qp);
    enq(qp, 5);
    display(qp);
    enq(qp, 5);
    display(qp);
    enq(qp, 5);
    display(qp);
    enq(qp, 5);
    display(qp);
    enq(qp, 5);
    display(qp);
    printf("%d\n", deq(qp));
    printf("%d\n", deq(qp));
    printf("%d\n", deq(qp));
    printf("%d\n", deq(qp));
    printf("%d\n", deq(qp));
    printf("%d\n", deq(qp));
}

// 5	
// 5	5	
// 5	5	5	
// 5	5	5	5	
// 5	5	5	5	5	
// Q Full
// 5	5	5	5	5	
// 5
// 5
// 5
// 5
// Q empty
// -99
// Q empty
// -99