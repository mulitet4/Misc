#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    int data;
    struct node* l;
    struct node* r;
} Node;

Node* createNode(int data){
    Node* n = (Node*) malloc(sizeof(Node));
    n->l = n->r = NULL;
    n->data = data;
    return n;
}

Node* addNode(Node* root, int data, char* dir){
    Node* newNode = createNode(data);
    Node* temp = root;
    for(int i = 0; i < strlen(dir) - 1; i++){
        if(dir[i] == 'l') temp = temp->l;
        else temp = temp->r;
    }
    if(dir[strlen(dir) - 1] == 'l'){
        temp->l = newNode;
    } else {
        temp->r = newNode;
    }
    
    return root;
}

void preorder(Node* root){
    if(root == NULL) return;
    printf("%d", root->data);
    preorder(root->l);
    preorder(root->r);
}

void postorder(Node* root){
    if(root == NULL) return;
    postorder(root->l);
    postorder(root->r);
    printf("%d", root->data);
}

// TODO Level Order

Node* copyTree(Node* root){
    if(root == NULL) return NULL;
    Node* newRoot = createNode(root->data);
    newRoot->l = copyTree(root->l);
    newRoot->r = copyTree(root->r);
    return newRoot;
}

int isEqual(Node* root1, Node* root2){
    if(root1 == NULL && root2 == NULL) return 1;
    if(root1 == NULL || root2 == NULL) return 0;
    return (root1->data == root2->data) && isEqual(root1->l, root2->l) && isEqual(root1->r, root2->r);
}

int searchTree(Node* root, int key){
    if(root == NULL) return 0;
    if(root->data == key) return 1;
    int searchL = searchTree(root->l, key);
    if(searchL) return 1;
    int searchR = searchTree(root->r, key);
    return searchR;
}

void main(){
    Node* root = createNode(1);
    root = addNode(root, 5, "l");
    root = addNode(root, 6, "r");
    root = addNode(root, 7, "ll");
    root = addNode(root, 8, "lr");
    preorder(root); printf("\n");
    postorder(root); printf("\n");
    Node* root2 = copyTree(root);
    int isEq = isEqual(root, root2);
    printf("%d\n", isEq);
    printf("%d\n", searchTree(root, 10));
    printf("%d\n", searchTree(root, 6));
}