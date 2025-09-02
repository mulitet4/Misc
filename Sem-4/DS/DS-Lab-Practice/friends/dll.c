#include<stdio.h>
#include<stdlib.h>

typedef struct node {
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

void insert(Node **head, int x) {
    Node *n = createNode(x);
    if (*head == NULL) {
        *head = n;
        return;
    }
    Node *temp = *head;
    while (temp->right != NULL) {
        temp = temp->right;
    }
    temp->right = n;
    n->left = temp;
}

void insertatbg(Node **head, int x) {
    Node *newn = createNode(x);
    if (*head == NULL) {
        *head = newn;
        return;
    }
    Node *temp = *head;
    newn->right = temp;
    temp->left = newn;
    (*head) = (*head)->left;
}

void insertatpos(Node **head, int x, int pos) {
    Node* newn = createNode(x);
    int i = 1;
    Node *temp = *head;
    Node *prev = NULL;

    while (i != pos - 1) {
        prev = temp;
        temp = temp->right;
        i++;
    }

    if (prev == NULL) {
        printf("Invalid position\n");
        free(newn);
        return;
    }

    prev->right = newn;
    newn->left = prev;
    newn->right = temp;

    if (temp != NULL) {
        temp->left = newn;
    }
}

void delete_e(Node *head) {
    Node *temp = head;
    while (temp->right != NULL) {
        temp = temp->right;
    }

    temp->left->right = NULL;
    free(temp);
}

void del_b(Node **head) {
    Node *temp = *head;
    temp->right->left = NULL;
    (*head) = (*head)->right;
    free(temp);
}

void del_p(Node *head, int pos) {
    int i = 1;
    Node *temp = head;
    Node *prev = NULL;

    while (i != pos && temp != NULL) {
        prev = temp;
        temp = temp->right;
        i++;
    }

    if (temp == NULL) {
        printf("Invalid position.\n");
        return;
    }

    if (prev != NULL) {
        prev->right = temp->right;
    }

    if (temp->right != NULL) {
        temp->right->left = prev;
    }

    free(temp);
}

void display(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->right;
    }
    printf("NULL\n");
}

void deleteDuplicates(Node *head) {
    Node *current = head;
    Node *temp;
    while (current != NULL && current->right != NULL) {
        if (current->data == current->right->data) {
            temp = current->right;
            current->right = temp->right;
            if (temp->right != NULL) {
                temp->right->left = current;
            }
            free(temp);
        } else {
            current = current->right;
        }
    }
}

void createcll(Node **head, int x) {
    Node *newn = createNode(x);

    if (*head == NULL) {  // If the list is empty
        *head = newn;
        newn->right = newn;  // Point to itself (circular)
        newn->left = newn;   // Point to itself (circular)
        return;
    }

    Node *temp = *head;
    while (temp->right != *head) {  // Traverse till we reach the last node (which points to the head)
        temp = temp->right;
    }

    temp->right = newn;  // Last node's right points to the new node
    newn->left = temp;   // New node's left points to the last node
    newn->right = *head; // New node's right points to the head (circular)
    (*head)->left = newn; // Head's left points to the new node (circular)
}

void displayc(Node* head) {
    if (head == NULL) {
        printf("The list is empty.\n");
        return;
    }

    Node* temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->right;
    } while (temp != head);  // Stop when we loop back to the head

    printf("Back to head\n");
}
Node* addCDLL(Node* head1, Node* head2) {
    Node *result = NULL;
    int carry = 0;

    Node *temp1 = head1;
    Node *temp2 = head2;

    do {
        // Extract data from both lists
        int sum = carry;
        if (temp1 != NULL) sum += temp1->data;
        if (temp2 != NULL) sum += temp2->data;

        // Compute the new carry and the digit to store
        carry = sum / 10;
        int digit = sum % 10;

        // Insert the digit into the result list
        createcll(&result, digit);

        // Move to the next node in both lists
        if (temp1 != NULL) temp1 = temp1->right;
        if (temp2 != NULL) temp2 = temp2->right;
    } while (temp1 != head1 || temp2 != head2);  // Continue until both lists are fully processed

    // If there's a carry left, add it as a new node
    if (carry != 0) {
        createcll(&result, carry);
    }

    return result;
}
void reverse(Node*head){
    if(head==NULL){
        return ;
    }
    reverse(head->right);
    printf("%d",head->data);
}

void reverse_r(Node **head) {
    Node* curr = *head;
    Node* temp = NULL;

    while (curr != NULL) {
        temp = curr->left;
        curr->left = curr->right;
        curr->right = temp;
        curr = curr->left;
    }

    if (temp != NULL) {
        *head = temp->left;
    }
}
int exists(Node *head,int v){
    Node *temp=head;
    while(temp!=NULL){
        if(temp->data==v){
            return 1;
        }
        temp=temp->right;

    }
    return 0;


}
Node* union1(Node *head1,Node *head2){
    Node *res=NULL;
    Node *temp1=head1;
    while(temp1!=NULL){
        insert(&res,temp1->data);
        temp1=temp1->right;

    }

    Node *temp2=head2;
    while(temp2!=NULL){
        if(!exists(res,temp2->data)){
            insert(&res,temp2->data);
        }
    }
    return res;
}
Node* intersection(Node *head1,Node *head2){
    Node *temp=head1;
    Node *res=NULL;
    while(temp!=NULL){
        if(exists(head2,temp->data)){
                if(!exists(res,temp->data)){
                    insert(&res,temp->data);
                }

        }
        temp=temp->next;
    }
    return res;
}




int main() {
    /*Node *head = NULL;
    insert(&head, 1);
    insert(&head, 1);
    insert(&head, 1);
    insert(&head,2);
    display(head);
    printf("reverse\n");
    reverse_r(&head);
    display(head);*/


    // Create circular DLL
    /*Node *headc = NULL;
    createcll(&headc, 2);
    createcll(&headc, 7);
    createcll(&headc, 9);
    displayc(headc);

     Node *num1 = NULL;
    Node *num2 = NULL;
//exists funcrtion automatically checks if data is there or not just need to provide header node
    // Representing the number 1234 (digits stored in reverse order)
    insertAtEnd(&num1, 4);
    insertAtEnd(&num1, 3);
    insertAtEnd(&num1, 2);
    insertAtEnd(&num1, 1);

    // Representing the number 987 (digits stored in reverse order)
    insertAtEnd(&num2, 7);
    insertAtEnd(&num2, 8);
    insertAtEnd(&num2, 9);

    printf("First number (num1): ");
    display(num1);

    printf("Second number (num2): ");
    display(num2);

    Node *sum = addCDLL(num1, num2);

    printf("Sum: ");
    display(sum);*/
    Node* list1 = NULL;
    Node* list2 = NULL;

    // Create first doubly linked list
    insert(&list1, 10);
    insert(&list1, 20);
    insert(&list1, 30);
    insert(&list1, 40);

    // Create second doubly linked list
    insert(&list2, 30);
    insert(&list2, 40);
    insert(&list2, 50);
    insert(&list2, 60);

    Node *r=union1(list1,list2);
    display(r);
    Node *i=intersection(list,list2);


    return 0;
}
