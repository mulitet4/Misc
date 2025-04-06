#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 256

void createtable(char* patt, int shift_table[]){
  for(int i = 0; i < MAX; i++){
    shift_table[i] = strlen(patt);
  }
  for(int i = 0; i < strlen(patt) - 1; i++){
    shift_table[(unsigned char)patt[i]] = strlen(patt) - 1 - i;
  }
}

void horspool(char* text, char* patt){
  int shift_table[MAX];
  createtable(patt, shift_table);
  int i = 0;
  while( i <= strlen(text) - strlen(patt)){
    int j = strlen(patt) - 1;
    while(j >= 0 && patt[j] == text[i + j]) j--;
    if(j < 0){
      printf("Pattern found at index: %d", i);
      i += shift_table[(unsigned char)text[i + strlen(patt)]];
    } else {
      i += shift_table[(unsigned char)text[i + strlen(patt) - 1]];
    }
  }
}

void main(){
  // char text[200];
  // char patt[100];
  // fgets(text, 200, stdin);
  // fgets(patt, 100, stdin);
  char* text = "aryan";
	char* patt = "ya";
  horspool(text, patt);
}