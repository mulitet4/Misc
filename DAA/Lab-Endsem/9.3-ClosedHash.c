#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_KEY_LEN 20
#define TABLE_SIZE 10

typedef struct table {
  int size;
  char** table;
} Table;

int hash(char* key, int size){
  return strlen(key) % size;
}

Table* createTable(int size){
  Table* t = (Table*) malloc(sizeof(Table));
  t->size = size;
  t->table = (char**) malloc(sizeof(char*) * size);
  for(int i = 0; i < size; i++){
    t->table[i] = NULL;
  }
  return t;
}

void insert(Table* t, char* key){
  int idx = hash(key, t->size);
  int og_idx = idx;
  while(t->table[idx] != NULL){
    idx = (idx + 1) % t->size;
    if(idx == og_idx){
      printf("Table full");
      return;
    }
  }
  t->table[idx] = strdup(key);
}

void search(Table* t, char* key){
  int idx = hash(key, t->size);
  int og_idx = idx;
  while(strcmp(t->table[idx], key) != 0){
    idx = ( idx + 1 ) % t->size;
    if(idx == og_idx) {
      printf("Not found\n");
      return;
    }
  }
  printf("Key found at idx: %d", idx);
}


void main(){
	int m; scanf("%d", &m);
	Table* ht = createTable(m);
	insert(ht, "hello");
	insert(ht, "world");
	search(ht, "world");
}
