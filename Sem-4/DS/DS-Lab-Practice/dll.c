#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* l;
    struct node* r;
} Node;

Node* createNode(int data){
    Node* n = (Node*) malloc(sizeof(Node));
    n->data = data;
    n->l=n->r=NULL;
    return n;
}

Node* insertb(Node* start, int data){
    Node* newNode = createNode(data);
    if(start == NULL){return newNode;}
    
    Node* temp = start;
    while(temp->r != NULL){temp = temp->r;}
    
    temp->r = newNode;
    newNode->l = temp;
    return start;
}

Node* insertf(Node* start, int data){
    Node* n = createNode(data);
    if(start == NULL) return n;
    n->r = start;
    start->l = n;
    return n;
}

Node* insertp(Node* start, int pos, int data){
    Node* newNode = createNode(data);
    Node* temp = start;
    for(int i = 1; i < pos - 1; i++){
        temp = temp->r;
    }
    newNode->r = temp->r;
    newNode->l = temp;
    temp->r = newNode;
    newNode->r->l = newNode;
    return start;
}

Node* deletef(Node* start){
    Node* temp = start->r;
    temp->l=NULL;
    free(start);
    return temp;
}

Node* deleteb(Node* start){
    Node* temp = start;
    while(temp->r->r != NULL) temp = temp->r;
    Node* todel = temp->r;
    temp->r = NULL;
    free(todel);
    return start;
}

Node* deletep(Node* start, int pos){
    Node* temp = start;
    for(int i = 1; i < pos; i++){
        temp = temp->r;
    }
    Node* todel = temp->r;
    temp->r = todel->r;
    todel->r->l = temp;
    free(todel);
    return start;
}

void display(Node* start){
    Node* temp = start;
    while(temp != NULL){
        printf("<-%d->", temp->data);
        temp = temp->r;
    }
}

Node* deleteDuplicates(Node* start){
    int u_elems[100]; int tos1 = -1;
    int to_delete_index[100]; int tos2 = -1;
    Node* temp = start; int pos = -1;
    while(temp != NULL){
        ++pos;
        if(tos1 == -1){
            u_elems[++tos1] = temp->data;
            temp = temp->r;
            continue;
        }
        for(int i = 0; i <= tos1; i++){
            if(u_elems[i] == temp->data){
                to_delete_index[++tos2] = pos;
            } else {
                u_elems[++tos1] = temp->data;
            }
        }
    }
    for(int i = 0; i < tos2; i++){
        start = deletep(start, to_delete_index[i]);
    }
    
    return start;
}

Node* reverse(Node* start){
    Node* temp = start;
    Node* newHead = NULL;
    
    while(temp != NULL){
        Node* next = temp->r;
        Node* prev = temp->l;
        temp->r = prev;
        temp->l = next;
        newHead = temp;
        temp = next;
    }
    
    return newHead;
}

void main(){
    Node* root = createNode(5);
    root = insertf(root, 10);
    root = insertf(root, 30);
    root = insertf(root, 50);
    root = insertp(root, 3, 66);
    root = insertp(root, 3, 20);
    root = insertp(root, 3, 20);
    root = insertp(root, 3, 20);
    display(root); printf("\n");
    root = deletef(root);
    root = deleteb(root);
    display(root);printf("\n");
    root = reverse(root);
    display(root);printf("\n");
}

// <-50-><-30-><-20-><-20-><-20-><-66-><-10-><-5->
// <-30-><-20-><-20-><-20-><-66-><-10->
// <-10-><-66-><-20-><-20-><-20-><-30->