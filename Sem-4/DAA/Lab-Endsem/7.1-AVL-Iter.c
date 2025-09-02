#include <stdio.h>
#include <stdlib.h>
#define MAX(a, b) ((a) > (b) ? (a) : (b))

typedef struct node {
  struct node *l, *r;
  int data;
  int height;
} Node;

int height(Node* node){
  if(!node) return 0;
  else return node->height;
}

int balance(Node* node){
  if(!node) return 0;
  else return height(node->l) - height(node->r);
}

Node* newNode(int data){
  Node* n = (Node*) malloc(sizeof(Node));
  n->data = data;
  n->l = n->r = NULL;
  n->height = 1;
  return n;
}

Node* rightRotate(Node* y){
  Node* x = y->l;
  Node* T2 = x->r;
  x->r = y;
  y->l = T2;
  y->height = MAX(height(y->l), height(y->r)) + 1;
  x->height = MAX(height(x->l), height(x->r)) + 1;
  return x;
}

Node* leftRotate(Node* x){
  Node* y = x->r;
  Node* T2 = y->l;
  y->l = x;
  x->r = T2;
  y->height = MAX(height(y->l), height(y->r)) + 1;
  x->height = MAX(height(x->l), height(x->r)) + 1;
  return y;
}

Node* insert(Node* root, int data){
  Node* n = newNode(data);
  Node* stack[100]; int top = -1;
  if(!root) return n;
  
  Node* curr = root;
  Node* par = NULL;
  while(curr){
    stack[++top] = curr;
    par = curr;
    if(data < curr->data) curr = curr->l;
    else if(data > curr->data) curr = curr->r;
    else return root;
  }
  if(data < par->data) par->l = n;
  else par->r = n;
  
  while(top >= 0){
    curr = stack[top--];
    curr->height = 1 + MAX(height(curr->l), height(curr->r));
    printf("Balance of node %d = %d\n", curr->data, balance(curr));
    int bal = balance(curr);
    
    Node* rebalanced = curr;

    if(bal > 1 && balance(curr->l) >= 0){ rebalanced = rightRotate(curr); }
    if(bal < -1 && balance(curr->r) <= 0){ rebalanced = leftRotate(curr); }
    if(bal > 1 && balance(curr->l) < 0){
      curr->l = leftRotate(curr->l);
      rebalanced = rightRotate(curr);
    }
    if(bal < -1 && balance(curr->r) > 0){
      curr->r = rightRotate(curr->r);
      rebalanced = leftRotate(curr);
    }

    if(top >= 0){
      Node* parent = stack[top];
      if(parent->l == curr) parent->l = rebalanced;
      else parent->r = rebalanced;
    } else {
      root = rebalanced;
    }
  }
  return root;
}

void inorder(Node* n){
	if(!n) return;
	inorder(n->l);
	printf("%d ", n->data);
	inorder(n->r);
}

void printTree(Node* root, int space) {
  if (root == NULL) return;
  space += 5;
  printTree(root->r, space);
  for (int i = 5; i < space; i++) printf(" ");
  printf("%d\n", root->data);
  printTree(root->l, space);
}


void main(){
	Node* root = NULL;
	printf("Enter nodes, -1 to stop\n");
	while(1){ 
		int n; scanf("%d", &n);
		if(n == -1) break;
		root = insert(root, n);
	}
	inorder(root);
  printf("\n");
  printTree(root, 0);
}
