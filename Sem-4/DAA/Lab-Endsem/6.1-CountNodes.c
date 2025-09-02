#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  struct node *l, *r;
  int data;
} Node;

Node* cn(int data){
  Node* n = (Node*) malloc(sizeof(Node));
  n->data = data; n->l = n->r = NULL;
  return n;
}

void countNodes(Node* root, int* count){
  if(root){
    countNodes(root->l, count);
    (*count)++;
    countNodes(root->r, count);
  }
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
  int count = 0;
  countNodes(root, &count);
  printf("%d", count);
}