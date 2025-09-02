#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#define MAX 5

typedef struct node{
    int data;
    struct node* next;
} Node;

Node* create(int data){
    Node* n = (Node*) malloc(sizeof(Node));
    n->data = data;
    n->next = NULL;
    return n;
}

Node* insertf(Node* start, int data){
    Node* newNode = create(data);
    newNode->next = start;
    return newNode;
}

Node* insertb(Node* start, int data){
    Node* newNode = create(data);
    Node* temp = start;
    while(temp->next != NULL){
        temp = temp->next;
    }
    temp->next = newNode;
    return start;
}

Node* insertp(Node* start, int pos, int data){
    Node* newNode = create(data);
    if(pos == 1){
        free(newNode);
        Node* newNode = insertf(start, data);
        return newNode; 
    }
    Node* temp = start;
    for(int i = 1; i < pos - 1; i++){
        temp = temp->next;
    }
    newNode->next = temp->next;
    temp->next = newNode;
    return start;
}

Node* inserto(Node* start, int data){
    Node* newNode = create(data);
    if(data < start->data){
        newNode = insertf(start, data);
        return newNode;
    }
    Node* temp = start;
    Node* prev = NULL;
    while(temp->next != NULL && data > temp->data){
        prev = temp;
        temp = temp->next;
    }
    prev->next = newNode;
    newNode->next = temp;
    return start;
}

Node* deletef(Node* start){
    Node* temp = start->next;
    free(start);
    return temp;
}

Node* deleteb(Node* start){
    Node* temp = start;
    while(temp->next->next != NULL){
        temp = temp->next;
    }
    Node* temp2 = temp->next;
    temp->next = NULL;
    free(temp2);
    return start;
}

Node* reverse(Node* start){
    Node* curr = start;
    Node* prev = NULL;
    while(curr != NULL){
        Node* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

void display(Node* start){
    Node* temp = start;
    while(temp != NULL){
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void main(){
    Node* start = create(0);
    start = insertf(start, 10);
    start = insertf(start, 20);
    start = insertb(start, 30);
    start = insertb(start, 50);
    display(start);
    start = insertp(start, 3, 60);
    display(start);
    start = deleteb(start);
    display(start);
    start = deletef(start);
    display(start);
    start = reverse(start);
    display(start);
}


// 20 10 0 30 50 
// 20 10 60 0 30 50 
// 20 10 60 0 30 
// 10 60 0 30 
// 30 0 60 10