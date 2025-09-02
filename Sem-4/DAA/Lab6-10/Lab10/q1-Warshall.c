#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void add_edge(int graph[MAX][MAX], int u, int v){
	graph[u][v] = 1;
}

void warshall(int graph[MAX][MAX], int n){
	int closure[MAX][MAX];
	for(int i = 0; i < n; i++)
		for(int j = 0; j < n; j++)
			closure[i][j] = graph[i][j];

	for(int k = 0; k < n; k++){
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				closure[i][j] = closure[i][j] || (closure[i][k] && closure[k][j]);
			}
		}
	}

	printf("Transitive Closure: \n");
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			printf("%d ", closure[i][j]);
		}
		printf("\n");
	}
}

void main(){
	int n;
	int graph[MAX][MAX];
	printf("Enter nodes: \n");
	scanf("%d", &n);
	printf("Enter edges as n n, -1 to stop\n");
	while(1){
		int m, n; 
		scanf("%d %d", &m, &n);
		if(m == -1) break;
		add_edge(graph, m, n);
	}
	warshall(graph, n);
}

// Enter nodes: 
// 3
// Enter edges as n n, -1 to stop
// 0 1
// 1 2
// -1 -1
// Transitive Closure: 
// 0 1 1 
// 0 0 1 
// 0 0 0
