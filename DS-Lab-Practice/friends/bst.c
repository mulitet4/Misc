
#include <stdio.h>
#include <stdlib.h>

// Define the structure for a tree node
typedef struct node {
    int data;
    struct node* left;
    struct node* right;
} Node;

// Function to create a new node
Node* createNode(int value) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to insert a node in the BST iteratively
Node* create_bst(Node* root, int value) {
    Node* newn = createNode(value);
    if (root == NULL) {
        return newn;
    }

    Node* par = NULL;
    Node* curr = root;

    while (curr != NULL) {
        par = curr;
        if (value < curr->data) {
            curr = curr->left;
        } else {
            curr = curr->right;
        }
    }

    if (value < par->data) {
        par->left = newn;
    } else {
        par->right = newn;
    }

    return root;
}

// In-order traversal to display the tree
void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

// Function to find the maximum node in the left subtree iteratively
Node* findmax(Node* root) {
    Node* curr = root;
    while (curr->right != NULL) {
        curr = curr->right;
    }
    return curr;
}

// Function to find the minimum node
Node *findmin(Node *root) {
    Node *temp = root;
    while (temp->left != NULL) {
        temp = temp->left;
    }
    return temp;
}

// Function to delete a node iteratively
Node* deleteNode(Node* root, int value) {
    Node* par = NULL;
    Node* curr = root;

    // Find the node to be deleted and its parent
    while (curr != NULL && curr->data != value) {
        par = curr;
        if (value < curr->data) {
            curr = curr->left;
        } else {
            curr = curr->right;
        }
    }

    if (curr == NULL) {
        printf("Value not found\n");
        return root;
    }

    // Case 1: Node with no children
    if (curr->left == NULL && curr->right == NULL) {
        if (par == NULL) {
            free(curr);
            return NULL;
        }

        if (par->left == curr) {
            par->left = NULL;
        } else {
            par->right = NULL;
        }
        free(curr);
    }
    // Case 2: Node with one child
    else if (curr->left == NULL || curr->right == NULL) {
        Node* child = (curr->left != NULL) ? curr->left : curr->right;

        if (par == NULL) {
            free(curr);
            return child;
        }

        if (par->left == curr) {
            par->left = child;
        } else {
            par->right = child;
        }
        free(curr);
    }
    // Case 3: Node with two children
    else {
        Node* maxNode = findmax(curr->left);
        int maxValue = maxNode->data;
        root = deleteNode(root, maxValue);  // Delete the max node
        curr->data = maxValue;              // Replace with max value
    }

    return root;
}

// Function to find the in-order successor of a node
Node* inorderSuccessor(Node* root, Node* target, Node* successor) {
    if (root == NULL) {
        return successor;
    }

    if (target->data < root->data) {
        successor = root;  // Potential successor
        return inorderSuccessor(root->left, target, successor);
    } else if (target->data > root->data) {
        return inorderSuccessor(root->right, target, successor);
    } else {
        // If target node has a right subtree
        if (target->right != NULL) {
            return findmin(target->right);
        }
    }

    return successor;
}

// Function to print the path to a node
int print(Node *root, int k) {
    if (root == NULL) {
        return 0;
    }

    if (root->data == k) {
        printf("%d ", root->data);
        return 1;
    }

    if (print(root->left, k) || print(root->right, k)) {
        printf("%d ", root->data);
        return 1;  // Don't forget this
    }

    return 0;
}

// Function to search a node in the BST
// Function to search for a node in the BST
Node* search(Node* root, int key) {
    // Base case: root is null or the key is found
    if (root == NULL || root->data == key) {
        return root;
    }
    //return root when null also


    // Key is smaller than root's data, search in the left subtree
    if (key < root->data) {
        return search(root->left, key);
    }

    // Key is greater than root's data, search in the right subtree
    return search(root->right, key);
}

// Main function to test all the functionalities
int main() {
    Node* root = NULL;

    // Insert elements into the BST
    root = create_bst(root, 50);
    root = create_bst(root, 30);
    root = create_bst(root, 70);
    root = create_bst(root, 20);
    root = create_bst(root, 40);
    root = create_bst(root, 60);
    root = create_bst(root, 80);

    // Display the elements of BST in in-order traversal
    printf("In-order traversal of BST: ");
    inorder(root);
    printf("\n");

    // Find the in-order successor for a specific node
    Node* target = root->left->right;  // Node with value 40
    Node* succ = inorderSuccessor(root, target, NULL);
    if (succ != NULL) {
        printf("In-order successor of %d is %d\n", target->data, succ->data);
    } else {
        printf("In-order successor of %d does not exist\n", target->data);
    }

    // Print path to node with value 40
    printf("Path to 40: ");
    if (!print(root, 40)) {
        printf("Node 40 not found\n");
    }

    // Search for node 40
    Node* s = search(root, 70);
    if (s) {
        printf("Node   found\n");
    } else {
        printf("Node   not found\n");
    }

    return 0;
}
