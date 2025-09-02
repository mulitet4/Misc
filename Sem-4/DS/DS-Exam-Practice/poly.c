#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define MAX 5

typedef struct node {
    int c;
    int e;
    struct node* next;
} Node;

Node* create(int c, int e){
    Node* n = (Node*) malloc(sizeof(Node));
    n->c = c; n->e = e;
    n->next = NULL;
    return n;
}

Node* insertb(Node* start, int c, int e){
    Node* n = create(c, e);
    if(!start){
        return n;
    }
    Node* temp = start;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = n;
    return start;
}

Node* add(Node* p1, Node* p2){
    Node* a = p1; Node* b = p2;
    Node* res = NULL;
    while(a != NULL && b != NULL){
        if(a->e < b->e){
            res = insertb(res, b->c, b->e);
            b = b->next;
        }
        else if(a->e == b->e){
            if((a->c + b->c) != 0){
                res = insertb(res, a->c + b->c, a->e);
            }
            a = a->next; b = b->next;
        }
        else if(a->e > b->e){
            res = insertb(res, a->c, a->e);
            a = a->next;
        }
    }
    while(a != NULL){
        res = insertb(res, a->c, a->e);
        a = a->next;
    }
    while(b != NULL){
        res = insertb(res, b->c, b->e);
        b = b->next;
    }
    return res;
}

Node* mult(Node* p1, Node* p2){
    Node* a = p1;
    Node* res = NULL;
    while(a != NULL){
        Node* b = p2;
        while(b != NULL){
            res = insertb(res, a->c * b->c, a->e + b->e);
            b = b->next;
        }
        a = a->next;
    }
    return res;
}

void display(Node* start){
    Node* temp = start;
    while(temp != NULL){
        printf("%dx^%d + ", temp->c, temp->e);
        temp = temp->next;
    }
    printf("\n");
}

void main(){
    Node* p1 = NULL;
    Node* p2 = NULL;
    p1 = insertb(p1, -1, 3);
    p1 = insertb(p1, 20, 2);
    p1 = insertb(p1, 10, 1);
    p2 = insertb(p2, 1, 4);
    p2 = insertb(p2, 1, 3);
    p2 = insertb(p2, 10, 1);
    Node* res = add(p1, p2);
    Node* res2 = mult(p1, p2);
    display(p1);
    display(p2);
    display(res);
    display(res2);
}


// -1x^3 + 20x^2 + 10x^1 + 
// 1x^4 + 1x^3 + 10x^1 + 
// 1x^4 + 20x^2 + 20x^1 + 
// -1x^7 + -1x^6 + -10x^4 + 20x^6 + 20x^5 + 200x^3 + 10x^5 + 10x^4 + 100x^2 + 