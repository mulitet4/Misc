#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *l;
    struct node *r;
    int height;
    struct node *par;
} Node;

Node *createNode(int data) {
    Node* n = (Node*) malloc(sizeof(Node));
    n->data = data; n->l = n->r = NULL; n->height = 0;
    n->par = NULL; return n;
}

int geth(Node* n) { if (!n) return 0; return n->height; }
int getbal(Node* n) { if (!n) return 0; return geth(n->r) - geth(n->l); }
int findMaxHeight(Node* n) { return geth(n->l) > geth(n->r) ? geth(n->l) : geth(n->r); }

Node* rightRotate(Node* n) {
    Node* child = n->l;
    Node* gchild = child->r;
    n->l = gchild;
    if (gchild) gchild->par = n;
    child->r = n;
    n->par = child;
    n->height = 1 + findMaxHeight(n);
    child->height = 1 + findMaxHeight(child);
    return child;
}

Node* leftRotate(Node* n) {
    Node* child = n->r;
    Node* gchild = child->l;
    child->l = n;
    n->par = child;
    n->r = gchild;
    if (gchild) gchild->par = n;
    n->height = 1 + findMaxHeight(n);
    child->height = 1 + findMaxHeight(child);
    return child;
}

Node* insert(Node* root, int data) {
    Node* n = createNode(data);
    if (!root) return n;
    Node* curr = root;
    Node* par = NULL;
    while (curr != NULL) {
        par = curr;
        if (data == curr->data) { printf("Duplicate\n"); return root; }
        if (data < curr->data) curr = curr->l;
        else curr = curr->r;
    }
    if (data < par->data) par->l = n;
    else par->r = n;
    n->par = par;

    curr = par;
    while (curr->par != NULL) {
        curr->height = 1 + findMaxHeight(curr);
        int bal = getbal(curr);
        if (bal < -1 && data < curr->l->data) curr = rightRotate(curr); // LL case
        if (bal > 1 && data > curr->r->data) curr = leftRotate(curr); // RR case
        if (bal < -1 && data > curr->l->data) { // LR case
            curr->l = leftRotate(curr->l);
            curr = rightRotate(curr);
        }
        if (bal > 1 && data < curr->r->data) {
            curr->r = rightRotate(curr->r);
            curr = leftRotate(curr);
        }
        curr = curr->par;
    }
    return root;
}

void inorder(Node* n) {
    if (!n) return;
    inorder(n->l);
    printf("%d ", n->data);
    inorder(n->r);
}

Node* findSuccessor(Node* root, int key) {
    Node* current = root;
    Node* successor = NULL;

    while (current) {
        if (key < current->data) {
            successor = current; // potential successor
            current = current->l; // go left
        } else if (key > current->data) {
            current = current->r; // go right
        } else {
            // If the node has a right child, the successor is the leftmost node in the right subtree
            if (current->r) {
                successor = current->r;
                while (successor->l) {
                    successor = successor->l;
                }
            }
            break;
        }
    }
    return successor;
}

Node* findPredecessor(Node* root, int key) {
    Node* current = root;
    Node* predecessor = NULL;

    while (current) {
        if (key < current->data) {
            current = current->l; // go left
        } else if (key > current->data) {
            predecessor = current; // potential predecessor
            current = current->r; // go right
        } else {
            // If the node has a left child, the predecessor is the rightmost node in the left subtree
            if (current->l) {
                predecessor = current->l;
                while (predecessor->r) {
                    predecessor = predecessor->r;
                }
            }
            break;
        }
    }
    return predecessor;
}

int main() {
    Node* root = NULL;
    printf("Enter nodes, -1 to stop\n");
    while (1) {
        int n; scanf("%d", &n);
        if (n == -1) break;
        root = insert(root, n);
    }
    
    inorder(root);
    printf("\n");

    int key;
    printf("Enter a key to find its successor and predecessor: ");
    scanf("%d", &key);

    Node* successor = findSuccessor(root, key);
    Node* predecessor = findPredecessor(root, key);

    if (successor) {
        printf("Successor of %d is %d\n", key, successor->data);
    } else {
        printf("No successor found for %d\n", key);
    }

    if (predecessor) {
        printf("Predecessor of %d is %d\n", key, predecessor->data);
    } else {
        printf("No predecessor found for %d\n", key);
    }

    return 0;
}
