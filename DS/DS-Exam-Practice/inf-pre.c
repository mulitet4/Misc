#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char infix[50], prefix[50], stack[50];
int tos = -1;

void push(char a){
    stack[++tos] = a;
}

char pop(){
    return stack[tos--];
}

int precedence(char a){
    switch(a){
        case '+':
        case '-': return 1;
        case '%':
        case '*':
        case '/': return 2;
        case '^': return 3;
        default: return -1;
    }
}

void evaluate(){
    int j = 0;
    for(int i = 0; infix[i] != '\0'; i++){
        char symb = infix[i];
        if(symb == '('){
            push(symb);
        } else if(symb == ')'){
            while(stack[tos] != '('){
                prefix[j++] = pop();
            }
            // Remove the ( from stack
            pop(); 
        } else if(precedence(symb) != -1){
            while(precedence(stack[tos]) >= precedence(symb)){
                prefix[j++] = pop();
            }
            push(symb);
        } else {
            prefix[j++] = symb;
        }
    }
    while(tos != -1){
        prefix[j++] = pop();
    }
}

void main(){
    strcpy(infix, "(a/(b-c+d))*(e-a)*c");
    evaluate();
    printf("%s", prefix);
}