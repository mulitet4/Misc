#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* r;
    struct node* l;
} Node;

Node* createNode(int data){
    Node* n = (Node*) malloc(sizeof(Node));
    n->data = data;
    n->r = n->l = n;
    return n;
}

Node* insertf(Node* head, int data){
    Node* newNode = createNode(data);
    newNode->r = head->r;
    head->r->l = newNode;
    newNode->l = head;
    head->r = newNode;
    return head;
}

Node* insertb(Node* head, int data){
    Node* newNode = createNode(data);
    newNode->l = head->l;
    newNode->r = head;
    head->l->r = newNode;
    head->l = newNode;
    return head;
}

void display(Node* head){
    Node* temp = head->r;
    while(temp != head){
        printf("%d", temp->data);
        temp = temp->r;
    }
}

void main(){
    Node* head = createNode(0);
    head = insertf(head, 10);
    head = insertf(head, 20);
    head = insertb(head, 30);
    display(head);
}