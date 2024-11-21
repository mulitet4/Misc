#include<stdio.h>
#include<stdlib.h>
#define MAX 5

typedef struct {
    int front;
    int rear;
    int a[MAX];
} Q;

void enq(Q* q, int elem){
    if(q->rear == MAX-1){
        printf("Q full\n");
        return;
    }
    if(q->front == -1 && q->rear == -1){
        q->front = 0;
        q->a[++q->rear] = elem;
        return;
    }
    for(int i = 0; i <= q->rear; i++){
        if(elem > q->a[i]){
            // shift elements
            //     i
            // [4, 2, 1, j, ]
            // [4, 2, 2, 1, ]
            for(int j = q->rear + 1; j > i; j--){
                q->a[j] = q->a[j-1];
            }
            q->a[i] = elem;
            break;
        }
        else if(i == q->rear){
            q->a[i+1] = elem;
        }
    }
    q->rear++;
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

void display(Q*q){
    for(int i = 0; i < MAX; i++){
        printf("%d\t", q->a[i]);
    }
    printf("\n");
}

void main(){
    Q q;
    q.rear = q.front = -1;
    for(int i = 0; i < MAX; i++){
        q.a[i] = 0;
    }
    Q* qp = &q;
    enq(qp, 5);
    display(qp);
    enq(qp, 3);
    display(qp);
    enq(qp, 7);
    display(qp);
    enq(qp, 2);
    display(qp);
    enq(qp, 12);
    display(qp);
}

// 5	0	0	0	0	
// 5	3	0	0	0	
// 7	5	3	0	0	
// 7	5	3	2	0	
// 12	7	5	3	2