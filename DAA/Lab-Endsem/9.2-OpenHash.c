#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_KEY_LEN 20
#define MAX_VAL_LEN 100

typedef struct ll {
  char key[MAX_KEY_LEN];
  char val[MAX_VAL_LEN];
  struct ll* next;
} Node;

typedef struct table{
  int size;
  Node** table;
} Table;

int hash(char* key, int size){
  return strlen(key) % size;
}

Table* createTable(int size){
  Table* t = (Table*) malloc(sizeof(Table));
  t->size = size;
  t->table = (Node**) malloc(sizeof(Node*) * size);
  for(int i = 0; i < size; i++){
    t->table[i] = NULL;
  }
  return t;
}

void insert(Table* t, char* key, char* val){
  int idx = hash(key, t->size);
  Node* newNode = (Node*) malloc(sizeof(Node));
  strcpy(newNode->key, key);
  strcpy(newNode->val, val);
  newNode->next = t->table[idx];
  t->table[idx] = newNode;
}

char* search(Table* t, char* key){
  int idx = hash(key, t->size);
  Node* curr = t->table[idx];
  while(curr){
    if(strcmp(curr->key, key) == 0){
      return curr->val;
    }
    curr = curr->next;
  }
  return '\0';
}

int main(){
	int m; scanf("%d", &m);
	Table* t = createTable(m);
	insert(t, "hello", "world");
	printf("%s", search(t, "hello"));
}