#include <stdio.h>
#include <string.h>
#define MAX 100

typedef struct {
    int tos;
    char a[MAX];
} Stack;

void push(Stack* s, char c){
    s->a[++s->tos] = c;
}

char pop(Stack* s){
    return s->a[s->tos--];
}

int isOperand(char c){
    int num = (int) c - '0';
    if(num >= 0 && num <= 9){
        return 1;
    }
    return 0;
}

int isOperator(char c){
    switch(c){
        case '/':
        case '*':
        case '+':
        case '(':
        case '-': return 1;
        default: return 0;
    }
}

int precedence(char c){
    switch(c){
        case '/':
        case '*': return 2;
        case '+':
        case '-': return 1;
    }
}

int main() {
    Stack s;
    s.tos = -1;
    char infix[] = "1-2*3";
    char result[100];
    int last = -1;
    
    for(int i = 0; i < strlen(infix); i++){
        if(isOperand(infix[i])){
            result[++last] = infix[i];
        } else if(isOperator(infix[i])) {
            while(precedence(s.a[s.tos]) >= precedence(infix[i])){
                result[++last] = pop(&s);
            }
            push(&s, infix[i]);
        } else {
            while(s.a[s.tos] != '('){
                result[++last] = pop(&s);
            }
            pop(&s);
        }
    }
    
    while(s.tos != -1){
        result[++last] = pop(&s);
    }
    result[++last] = '\0';
    
    printf("%s", result);
}