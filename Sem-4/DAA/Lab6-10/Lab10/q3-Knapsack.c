#include <stdio.h>

int knapsack(int W, int weights[], int values[], int n) {
    int i, w;
    int K[n + 1][W + 1];
    for (i = 0; i <= n; i++) {
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                K[i][w] = 0; 
            } else if (weights[i - 1] <= w) {
                K[i][w] = (values[i - 1] + K[i - 1][w - weights[i - 1]] > K[i - 1][w]) ?
                           (values[i - 1] + K[i - 1][w - weights[i - 1]]) : K[i - 1][w];
            } else {      
                K[i][w] = K[i - 1][w];
            }
        }
    }
    return K[n][W]; 
}

int main() {
    int n, W, values[100], weights[100];
    printf("Enter no. of items:");
    scanf("%d", &n);
    printf("Enter the values:");
    for(int i = 0; i < n; i++) scanf("%d", &values[i]);
    printf("Enter the weights:");
    for(int i = 0; i < n; i++) scanf("%d", &weights[i]);
    printf("Enter the knap size:");
    scanf("%d", &W);     
    int maxValue = knapsack(W, weights, values, n);
    printf("Maximum value in Knapsack = %d\n", maxValue);
    return 0;
}
