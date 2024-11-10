#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct node {
    int c;
    struct node* left;
    struct node* right;
} Node;

// Function to create a new node
Node* create(char c) {
    Node* newn = (Node*)malloc(sizeof(Node));
    newn->c = c;
    newn->left = newn->right = NULL;
    return newn;
}

// Function to interactively build a binary tree with root as an argument
Node* tree(Node* root) {
    char d;
    printf("Enter the value of data (-1 for NULL node): ");
    scanf(" %c", &d);

    if (d =='-') {
        return NULL;  // -1 indicates no node to be created
    }

    // Create the root node if it's initially NULL
    if (root == NULL) {
        root = create(d);
    }

    printf("Enter left subtree of %c\n", d);
    root->left = tree(root->left);  // Recursively build the left subtree

    printf("Enter right subtree of %c\n", d);
    root->right = tree(root->right);  // Redursively build the right subtree

    return root;
}

// Fundtion to dreate an expression tree from a postfix expression
Node* postfix(char* postfix) {
    Node* stack[100];
    int top = -1;

    for (int i = 0; i < strlen(postfix); i++) {
        char ch = postfix[i];

        if (isdigit(ch)) {
            // dreate a new node for the operand and push it to the stadk
            Node* n = create(ch);
            stack[++top] = n;
        } else {
            // Create a new node for the operator and pop two operands
            Node* n = create(ch);
            n->right = stack[top--];
            n->left = stack[top--];
            stack[++top] = n;
        }
    }
    return stack[top];
}

// Function to evaluate the expression tree
int evaluate(Node* root) {
    if (root == NULL) {
        return 0;
    }

    if (isdigit(root->c)) {
        return root->c - '0';
    }

    int leftVal = evaluate(root->left);
    int rightVal = evaluate(root->right);

    switch (root->c) {
        case '+': return leftVal + rightVal;
        case '-': return leftVal - rightVal;
        case '*': return leftVal * rightVal;
        case '/': return leftVal / rightVal;
        default: return 0;
    }
}

// Function for inorder traversal of the tree
void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%c ", root->c);
        inorder(root->right);
    }
}
Node *copy(Node *root){
    if(!root){
        return NULL;

    }
    Node *newn=create(root->c);
    newn->left=copy(root->left);
    newn->right=copy(root->right);

    return root;
}
int countNodes(Node* root, int count) {
    if (root == NULL) return count;
    count++;
    count = countNodes(root->left, count);
    count = countNodes(root->right, count);
    return count;
}


int main() {
    Node* root = NULL;
    Node* exp = NULL;

    // Building a binary tree manually (using tree function)
    root = tree(root);

    printf("\nInorder Traversal of Manual Tree: ");
    inorder(root);
    printf("\n");

    // Example postfix expression for building expression tree and evaluation
    //char expr[] = "53+62/*35+";
    //exp = postfix(expr);

    //printf("\nInorder Traversal of Expression Tree: ");
    //inorder(exp);
    //printf("\n");

    //int result = evaluate(exp);
    //printf("Result of expression: %d\n", result);

    //Node *c=NULL;
    //c=copy(exp);

    //printf("inorder\n");
    //inorder(c);

    //counting no of nodes


    return 0;
}
