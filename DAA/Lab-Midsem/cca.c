#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int data;
  struct node *l, *r;
} Node;

Node* cn(int data){
  Node* n = (Node*) malloc(sizeof(Node));
  n->data = data; n->l = n->r = NULL;
  return n;
}

Node* cca(Node* root, int a, int b){
  if(root == NULL || root->data == a || root->data == b) return root;
  Node* left = cca(root->l, a, b);
  Node* right = cca(root->r, a, b);
  if(left == NULL) return right;
  else if(right == NULL) return left;
  else return root;
}

int main(){
  Node* root = cn(1);
  root->l = cn(2);
  root->l->r = cn(5);
  root->l->l = cn(4);
  root->r = cn(3);
  root->r->l = cn(6);
  root->r->r = cn(7);
  root->r->r->l = cn(8);
  printf("%d", (cca(root, 6, 8))->data);
}