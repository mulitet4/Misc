#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_KEY_LEN 20
#define MAX_VAL_LEN 100

typedef struct ll {
	char key[MAX_KEY_LEN];
	char val[MAX_VAL_LEN];
	struct ll* next;
} Entry;

typedef struct table {
	int size;
	Entry** table;
} HashTable;

int hash(char* key, int size){ return strlen(key) % size; }

HashTable* createTable(int size){
	HashTable* ht = (HashTable*) malloc(sizeof(HashTable));
	ht->size = size;
	ht->table = (Entry**) malloc(sizeof(Entry*) * size);
	for(int i = 0; i < size; i++) { ht->table[i] = NULL; }
	return ht;
}

void insert(HashTable* ht, char* key, char* val){
	int idx = hash(key, ht->size);
	Entry* new_entry = malloc(sizeof(Entry));
	strcpy(new_entry->key, key);
	strcpy(new_entry->val, val);
	new_entry->next = ht->table[idx];
	ht->table[idx] = new_entry;
}

char* search(HashTable* ht, char* key){
	int idx = hash(key, ht->size);
	Entry* current = ht->table[idx];
	int opc = 0;

	while(current){
		opc++;
		if(strcmp(current->key, key) == 0) {
			printf("Successful Opcount: %d", opc);
			return current->val;
		}
		current = current->next;
	}
	printf("Unsuccessful Opcount: %d", opc);
	return '\0';
}

int main(){
	int m; scanf("%d", &m);
	HashTable* ht = createTable(m);
	insert(ht, "hello", "world");
	printf("%s", search(ht, "hello"));
}
