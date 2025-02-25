#include <stdio.h>
#include <stdlib.h>

int opcount = 0;

struct node {
    int data;
    struct node *r, *l;
};

typedef struct node* Node;

Node newNode(int data){
    Node n = (Node) malloc(sizeof(struct node));
    n->data = data;
    n->l = n->r = NULL;
    return n;
}

int countNode(Node root){
    if(!root) return 0;
    opcount++;
    return 1 + countNode(root->l) + countNode(root->r);
}

int main(){
    Node root = newNode(10);
    root->r = newNode(5);
    root->r->r = newNode(12);
    root->r->l = newNode(15);
    printf("%d", countNode(root));
}