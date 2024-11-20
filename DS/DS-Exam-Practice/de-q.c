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
    printf("\nf:%d, r:%d\n", q->front, q->rear);
}

int isfull(Q* q){
    if(q->front == 0 && q->rear == MAX - 1){
        printf("Q Full\n");
        return 1;
    }
    return 0;
}

int isempty(Q* q){
    if(q->front == -1){
        printf("Q Empty\n");
        return 1;
    }
    return 0;
}

void pushf(Q* q, int x){
    if(isfull(q)) return;
    if(q->front == -1) {q->front = 0;}
    for(int i = q->rear; i >= q->front; i--){
        q->a[i+1] = q->a[i];
    }
    q->rear++;
    q->a[q->front] = x;
}

void pushb(Q* q, int x){
    if(isfull(q)) return;
    if(q->front == -1) q->front = 0;
    q->a[++q->rear] = x;
}

int removef(Q* q){
    if(isempty(q)) return -99;
    int temp = q->a[q->front];
    q->a[q->front] = 0;
    if(q->front == q->rear){
        q->front = q->rear = -1;
    } else {
        q->front++;
    }
    return temp;
}

int removeb(Q* q){
    if(isempty(q)) return -99;
    int temp = q->a[q->rear];
    q->a[q->rear] = 0;
    if(q->front == q->rear){
        q->front = q->rear = -1;
    } else {
        q->rear--;
    }
    return temp;
}

void main(){
    Q* q = (Q*) malloc(sizeof(Q));
    q->rear = q->front = -1;
    pushf(q, 10);
    display(q);
    pushf(q, 20);
    display(q);
    pushb(q, 30);
    display(q);
    pushb(q, 40);
    display(q);
    removef(q);
    display(q);
    removeb(q);
    display(q);
}

// 10 0 0 0 0 
// f:0, r:0
// 20 10 0 0 0 
// f:0, r:1
// 20 10 30 0 0 
// f:0, r:2
// 20 10 30 40 0 
// f:0, r:3
// 0 10 30 40 0 
// f:1, r:3
// 0 10 30 0 0 
// f:1, r:2