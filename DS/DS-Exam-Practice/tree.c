#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

typedef struct node{
    int data;
    struct node* l;
    struct node* r;
} Node;

Node* createNode(int data){
    Node* n = (Node*) malloc(sizeof(Node));
    n->r = n->l = NULL;
    n->data = data;
    return n;
}

Node* createT(Node* root, char* dir, int data){
    Node* n = createNode(data);
    Node* temp = root;
    int i = 0;
    for(i; i < strlen(dir) - 1; i++){
        if(dir[i] == 'l'){
            temp = temp->l;
        } else {
            temp = temp->r;
        }
    }
    if(dir[strlen(dir) - 1] == 'l'){
        temp->l = n;
    } else {
        temp->r = n;
    }
    return root;
}

void preorder(Node* root){
    if(root == NULL) return;
    printf("%d", root->data);
    preorder(root->l);
    preorder(root->r);
}

void inorder(Node* root){
    if(root == NULL) return;
    inorder(root->l);
    printf("%d ", root->data);
    inorder(root->r);
}

void iinorder(Node* root){
    Node* cur = root;
    Node* s[50];
    int tos = -1;
    while(1){
        while(cur != NULL){
            s[++tos] = cur;
            cur = cur->l;
        }
        if(tos == -1){
            return;
        }
        cur = s[tos--];
        printf("%d ", cur->data);
        cur = cur->r;
    }
}

void ipreorder(Node* root){
    Node* cur = root;
    Node* s[50];
    int tos = -1;
    s[++tos] = root;
    while(tos != -1){
        cur = s[tos--];
        printf("%d", cur->data);
        if(cur->l) s[++tos] = cur->l;
        if(cur->r) s[++tos] = cur->r;
    }
}

void levelorder(Node* root){
    Node* cur = root;
    Node* q[50];
    int rear = -1, front = 0;
    q[++rear] = cur;
    while(front <= rear){
        cur = q[front++];
        if(cur != NULL){
            printf("%d ", cur->data);
        }
        if(cur->l){
            q[++rear] = cur->l;
        }
        if(cur->r){
            q[++rear] = cur->r;
        } 
    }
}

void cinorder(Node* root){
    if(root == NULL) return;
    inorder(root->l);
    printf("%c ", root->data);
    inorder(root->r);
}

Node* createTPre(char* postfix){
    Node* s[50];
    int top = -1;
    for(int i = 0; i < strlen(postfix); i++){
        char symb = postfix[i];
        Node* n = createNode(symb);
        if(isalnum(symb)){
            s[++top] = n;
        } else {
            n->l = s[top--];
            n->r = s[top--];
            s[++top] = n;
        }
    }
    return s[top--];
}

void main(){
    Node* root = createNode(1);
    root = createT(root, "l", 10);
    root = createT(root, "r", 20);
    inorder(root);
    iinorder(root);
    levelorder(root);
    Node* root2 = createTPre("abc*+");
    cinorder(root2);
}

// 10 1 20 10 1 20 1 10 20 99 42 98 + 97