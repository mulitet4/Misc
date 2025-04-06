#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_KEY_LEN 20
#define TABLE_SIZE 10

typedef struct ht {
	int size;
	char** table;
} HashTable;

int hash(char* key, int size){
	return strlen(key) % size;
}

HashTable* createTable(int size){
	HashTable* ht = (HashTable*) malloc(sizeof(HashTable));
	ht->size = size;
	ht->table = (char**) malloc(sizeof(char*) * size);
	for(int i = 0; i < size; i++){ ht->table[i] = NULL; }
	return ht;
}

void insert(HashTable* ht, char* key){
	int idx = hash(key, ht->size);
	int og_idx = idx;
	while(ht->table[idx] != NULL){
		idx = (idx + 1) & ht->size;
		if(idx == og_idx){ printf("Hash Table full. -1"); return; }
	}
	ht->table[idx] = strdup(key);
}

int search(HashTable* ht, char* key){
	int idx = hash(key, ht->size);
	int og_idx = idx;
	int opc = 0;
	while(ht->table[idx] != NULL){
		opc++;
		if(strcmp(ht->table[idx], key) == 0) {
			printf("Successful Opcount: %d", opc);
			return 1;
		}
		idx = (idx + 1) % ht->size;
		if(idx == og_idx) break;
	}
	printf("Unsuccessful Opcount: %d", opc);
	return 0;
}

void main(){
	int m; scanf("%d", &m);
	HashTable* ht = createTable(m);
	insert(ht, "hello");
	insert(ht, "world");
	search(ht, "world");
}
