// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct {
    int a[MAX];
    int tos;
} Stack;

void push(Stack* s, int elem){
    if(s->tos == MAX){return;}
    s->a[++(s->tos)] = elem;
}

int pop(Stack* s){
    if(s->tos == -1){return -1;}
    return s->a[s->tos--];
}

void display(Stack* s){
    for(int i = s->tos; i >= 0; i--){
        printf("%d", s->a[i]);
    }
}

void main(){
    Stack* s = (Stack*) malloc(sizeof(Stack));
    s->tos = -1;
    int decimal;
    decimal = 20;
    while(decimal > 0){
        int temp = decimal%2;
        push(s, temp);
        decimal /= 2;
    }
    display(s);
}

// 10100