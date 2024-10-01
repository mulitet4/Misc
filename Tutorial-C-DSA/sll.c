#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int elem;
    struct node* next;
} Node;

Node* getNode(){
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->next = NULL;
    return newNode;
}

Node* insertAtStart(Node* head, int elem){
    Node* newNode = getNode();
    newNode->elem = elem;
    if(head == NULL){
        head = newNode;
        newNode->next = NULL;
        return head;
    }
    newNode->next = head;
    printf("%d", newNode->elem);
    head = newNode;
    return head;
}

Node* insertAtPos(Node* head, int pos, int elem){
    Node* newNode = getNode();
    newNode->elem = elem;
    if(head == NULL){
        return newNode;
    }
    Node* last = head;
    for(int i = 1; i < pos; i++){
        last = last->next;
    }
    newNode->next = last->next;
    last->next = newNode;
    return head;
}

Node* insertAtEnd(Node* head, int elem){
    Node* newNode = getNode();
    newNode->elem = elem;
    if(head == NULL){
        return newNode;
    }
    Node* last = head;
    while(last->next != NULL){
        last = last->next;
    }
    last->next = newNode;
    return head;
}

void display(Node* start){
  Node* temp;
  if(start == NULL){
    printf("Linked list is empty \n");
    return;
  }
  printf("Contents of the Linked List are \n");
  temp = start;
  while(temp!=NULL)
  {
    printf("|%d|%p|-->",temp->elem,temp->next);
    temp = temp->next;
  }
  printf("\n");
}

Node* deleteAtFront(Node* head){
    Node* temp = head;
    head = head->next;
    free(temp);
    return head;
}

Node* deleteAtRear(Node* head){
    Node* last = head;
    while(last->next->next != NULL){
        last = last->next;
    }
    Node* temp = last->next;
    last->next = NULL;
    free(temp);
    return head;
}

Node* deleteAtPos(Node* head, int pos){
    Node* last = head;
    for(int i = 1; i < pos; i++){
        last = last->next;
    }
    Node* temp = last->next;
    last->next = last->next->next;
    free(temp);
    return head;
}

void main(){
    Node* head = NULL;
    head = insertAtStart(head, 10);
    display(head);
    head = insertAtStart(head, 20);
    display(head);
    head = insertAtPos(head, 1, 30);
    display(head);
    head = insertAtPos(head, 1, 40);
    display(head);
    head = insertAtEnd(head, 50);
    display(head);
    head = deleteAtFront(head);
    display(head);
    head = deleteAtRear(head);
    display(head);
    head = deleteAtPos(head, 1);
    display(head);
}


// Contents of the Linked List are 
// |10|(nil)|-->
// 20Contents of the Linked List are 
// |20|0x1c912a0|-->|10|(nil)|-->
// Contents of the Linked List are 
// |20|0x1c916f0|-->|30|0x1c912a0|-->|10|(nil)|-->
// Contents of the Linked List are 
// |20|0x1c91710|-->|40|0x1c916f0|-->|30|0x1c912a0|-->|10|(nil)|-->
// Contents of the Linked List are 
// |20|0x1c91710|-->|40|0x1c916f0|-->|30|0x1c912a0|-->|10|0x1c91730|-->|50|(nil)|-->
// Contents of the Linked List are 
// |40|0x1c916f0|-->|30|0x1c912a0|-->|10|0x1c91730|-->|50|(nil)|-->
// Contents of the Linked List are 
// |40|0x1c916f0|-->|30|0x1c912a0|-->|10|(nil)|-->
// Contents of the Linked List are 
// |40|0x1c912a0|-->|10|(nil)|-->