#include <stdio.h>
#include <string.h>
#define MAX 100

typedef struct {
    int tos;
    char a[MAX];
} Stack;

int isOperand(char c){
    int num = (int) c - '0';
    if(num >= 0 && num <= 9){
        return 1;
    }
    return 0;
}

int eval(char op, char op1, char op2){
    int opi1 = (int) op1 - '0';
    int opi2 = (int) op2 - '0';
    switch(op){
        case '+': return opi2 + opi1; break;
        case '-': return opi2 - opi1; break;
        case '*': return opi2 * opi1; break;
        case '/': return opi2 / opi1; break;
        default: return 0; break;
    }
}

void push(Stack* s, char c){
    s->a[++s->tos] = c;
}

char pop(Stack* s){
    return s->a[s->tos--];
}

int main() {
    Stack s;
    s.tos = -1;
    char postfix[] = "123*-";
    for(int i = 0; i < strlen(postfix); i++){
        if(isOperand(postfix[i])){
            push(&s, postfix[i]);
        } else {
            char op1 = pop(&s);
            char op2 = pop(&s);
            int res = eval(postfix[i], op1, op2);
            char resc = (char) res + '0';
            push(&s, resc);
        }
    }
    printf("%d", (int) pop(&s) - '0');
    return 0;
}