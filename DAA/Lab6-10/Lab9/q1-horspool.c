#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 256

void createtable(char* pattern, int pattern_length, int shift_table[]){
	for(int i = 0; i < MAX; i++){
		shift_table[i] = pattern_length;
	}
	for(int i = 0; i < pattern_length - 1; i++){
		shift_table[(unsigned char)pattern[i]] = pattern_length - 1 - i;
	}
}

void horspool(char* text, char* pattern){
	int text_len = strlen(text);
	int patt_len = strlen(pattern);
	int shift_table[MAX];
	createtable(pattern, patt_len, shift_table);
	int i = 0;
	while( i <= text_len - patt_len){
		int j = patt_len - 1;
		while(j >= 0 && pattern[j] == text[i+j]) j--;
		if( j < 0 ){
			printf("Pattern found at index: %d\n", i);
			i += shift_table[(unsigned char) text[i + patt_len]];
		} else {
			i += shift_table[(unsigned char) text[i + patt_len - 1]];
		}
	}
}

void main(){
	char text[200];
	char patt[100];
	fgets(text, 200, stdin);
	fgets(patt, 100, stdin);
	// char* text = "acbcabcbdbabcbcabc";
	// char* patt = "abc";

	horspool(text, patt);
}
