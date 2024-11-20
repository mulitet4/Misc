#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node* l;
    struct node* r;
} Node;

Node* createNode(int data){
    Node* n = (Node*) malloc(sizeof(Node));
    n->data = data;
    n->l = n-> r = NULL;
    return n;
}

Node* insert(Node* root, int data){
    Node* newNode = createNode(data);
    Node* temp = root;
    Node* parent = root;
    while(temp != NULL){
        parent = temp;
        if(data > temp->data){
            temp = temp->r;
        } else {
            temp = temp->l;
        }
    }
    if(data > parent->data){
        parent->r = newNode;
    } else {
        parent->l = newNode;
    }
    
    return root;
}

void inorder(Node* root){
    if(root == NULL){return;}
    inorder(root->l);
    printf("%d ", root->data);
    inorder(root->r);
}

Node* deleteNode(Node* root, int elem){
    Node* parent = NULL;
    Node* temp = root;
    
    while(temp != NULL){
        parent = temp;
        if(temp->data == elem){break;}
        if(elem < temp->data) temp = temp -> l;
        else temp = temp -> r;
    }
    
    if(temp == NULL) {
        printf("Value not found");
        return root;
    }
    
    if(temp->l == NULL && temp->r == NULL){
        if(parent == NULL){
            free(temp);
            return NULL;
        }
        if(parent->r == temp) parent->r = NULL;
        else parent->l = NULL;
        free(temp);
    }
    
    else if(temp->l == NULL || temp->r == NULL){
        Node* child = temp->l == NULL? temp->r: temp->l;
        if(parent == NULL){
            free(temp);
            return child;
        }
        if(parent->r == temp) parent->r = child;
        else parent->l = child;
        free(temp);
    }
    
    else {
        Node* succ = temp->r;
        while(succ->l != NULL) succ = succ -> l;
        int succVal = succ->data;
        root = deleteNode(root, succVal);
        temp->data = succVal;
    }
    
    return root;
}

void main(){
    Node* root = createNode(5);
    root = insert(root, 10);
    root = insert(root, 3);
    root = insert(root, 1);
    root = insert(root, 4);
    inorder(root); printf("\n");
    root = deleteNode(root, 5); printf("\n");
    inorder(root);
}