#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  struct node *l, *r;
  int data;
} Node;

Node* create(int data){
  Node* n = (Node*) malloc(sizeof(Node));
  n->data = data;
  n->l = n->r = NULL;
  return n;
}

Node* insert(Node* root, int data){
  Node* n = create(data);
  if(root == NULL) return n;
  Node* par = NULL;
  Node* tr = root;
  while(tr){
    par = tr;
    if(data < tr->data) tr = tr->l;
    else if(data > tr->data) tr = tr->r;
    else {printf("Duplicate\n"); return root;}
  }
  if(data < par->data) par->l = n;
  else par->r = n;
  return root;
}

void inorder(Node* root){
  if(root){
    inorder(root->l);
    printf("%d", root->data);
    inorder(root->r);
  }
}

void main(){
  Node* root = insert(NULL, 5);
  root = insert(root, 3);
  root = insert(root, 6);
  root = insert(root, 9);
  inorder(root);
}