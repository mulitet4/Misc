#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int strmatch(char* text, char* patt){
  for(int i = 0; i < strlen(text); i++){
    int j = 0;
    while(text[i+j] == patt[j]) j++;
    if(j == strlen(patt) - 1) return i;
  }
  return -1;
}

void main(){
  char* text = "hello";
  char* patt = "lo";
  printf("%d", strmatch(text, patt) + 1);
}