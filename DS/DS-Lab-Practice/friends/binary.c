#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node* left;
    struct node* right;
} Node;


Node* createNode(int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

Node* tree(Node* root) {
    int x;
    printf("Enter value (-1 for no value): ");
    scanf("%d", &x);

    if (x == -1) {
        return NULL;
    }

    if (root == NULL) {
        root = createNode(x);
    }

    printf("Enter left subtree\n of %d",root->data);
    root->left = tree(root->left);

    printf("Enter right subtree\n");
    root->right = tree(root->right);

    return root;
}

void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}
Node *copy(Node *root){
    if(!root){
        return NULL;
    }
    Node *newr=createNode(root->data);
    newr->left=copy(root->left);
    newr->right=copy(root->right);

    return newr;//return newly created root
}
int count_nodes(Node *root){
    static int count=0;
    if(root!=NULL){
        count_nodes(root->left);
        count++;
        count_nodes(root->right);
    }
    return count;

}
int count_leafnodes(Node *root){
    static int count =0;
    if(root!=NULL){
        if(root->left==NULL && root->right==NULL){
            count++;

        }
        count_leafnodes(root->left);
        count_leafnodes(root->right);
    }
    return count;
}
int bin_search(Node *root,int ele){
    static int t=0;
    if(root){
        if(root->data==ele){

            t++;
            return t;
        }
        if(t==0){
            bin_search(root->left,ele);
        }
        if(t==0){
            bin_search(root->right,ele);
        }

    }

}
int isEqual(Node *root1,Node *root2){
    if(root1==NULL && root2==NULL){
        return 1;
    }
    if(root1==NULL || root2==NULL){
        return 0;
    }

    return (root1->data==root2->data)&&isEqual(root1->left,root2->right)&&isEqual(root1->right,root2->right);

}




int main() {
    Node* root = NULL;
    root = tree(root);
    printf("Inorder traversal of the tree: ");
    inorder(root);
    Node *r=NULL;
    r=copy(root);
    printf("\n");
    inorder(r);
    printf("\n");
    int nodes=count_nodes(root);
    printf("%d",nodes);
    int leaf=count_leafnodes(root);
    printf("%d",leaf);
    int e=isEqual(root,r);
    return 0;
}
