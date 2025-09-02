#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

char prefix[50], stack[50];
int tos = -1;

void push(char c){stack[++tos] = c;}
char pop(){return stack[tos--];}

int isop(char c){
    return (c == '+' || c == '-' || c == '/' || c == '*' || c == '^' || c == '%');
}

int calc(char op, int op1, int op2){
    switch(op){
        case '+': return op1 + op2; 
        case '-': return op1 - op2;
        case '*': return op1 * op2;
        case '/': return op1 / op2;
        case '^': return pow(op1, op2);
        case '%': return op1 % op2;
    }
}

int eval(){
    for(int i = 0; prefix[i] != '\0'; i++){
        char symb = prefix[i];
        if(isop(symb)){
            int op2 = pop() - '0';
            int op1 = pop() - '0';
            char res = calc(symb, op1, op2) + '0';
            push(res);
        } else {
            push(symb);
        }
    }
    return (pop() - '0');
}

void main(){
    strcpy(prefix, "153*+");
    int res = eval();
    printf("%d", res);
}