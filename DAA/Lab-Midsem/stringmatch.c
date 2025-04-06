#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int sm(char* text, char* pat){
  for(int i = 0; i < strlen(text); i++){
    int j = 0;
    int k = i;
    for(j; j < strlen(pat); j++, k++){
      if(pat[j] != text[k]) break;
    }
    if((j) == strlen(pat)) return i;
  }
  return -1;
}

void main(){
  char* text = "aryan";
  char* pat = "an";
  printf("%d", sm(text, pat) + 1);
}