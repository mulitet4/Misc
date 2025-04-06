#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	int data;
	struct node *l, *r;
} Node;

Node *newNode(int data) {
	Node* n = (Node*) malloc(sizeof(Node));
	n->data = data; n->l=n->r=NULL;
	return n;
}

Node *insert(Node *root, int data){
	Node* n = newNode(data);
	if(!root) return n;
	Node* temp = root;
	Node* parent = temp;
	while(temp != NULL){
		parent = temp;
		if(data == temp->data) {
			printf("Duplicate key found");
			return root;
		}
		if(data < temp->data) temp = temp->l;
		else temp = temp->r;
	}
	if(data < parent->data) parent->l = n;
	else parent->r = n;
	return root;
}

int countNodes(Node *root, int *opcount){
	if(root == NULL) return 0;
	(*opcount)++;
	return 1 + countNodes(root->l, opcount) + countNodes(root->r, opcount);
}

void main(){
	int count = 0, opcount = 0, *opc = &opcount;
	printf("Enter nodes, type -1 to stop");
	int inp = 0; Node* root = NULL;
	while(1){
		scanf("%d", &inp);
		if(inp == -1) break;
		root = insert(root, inp);
	}
	count = countNodes(root, opc);
	printf("Count: %d; Opcount: %d", count, opcount);
}
