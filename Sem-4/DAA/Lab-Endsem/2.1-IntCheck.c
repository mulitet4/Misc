#include <stdio.h>
#include <stdlib.h>

void main(){
  int n = 24;
  int m = 15;
  int min = n < m ? n : m;
  for(int i = min; i > 1; i--){
    if(n % i == 0 && m % i == 0) { printf("GCD: %d", i); break; }
  }
}