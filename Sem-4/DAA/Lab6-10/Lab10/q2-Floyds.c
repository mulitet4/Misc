#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void floyds(int graph[MAX][MAX], int n){
	int dist[n][n], i, j, k;
	for(i = 0; i < n; i++){
		for(j = 0; j < n; j++){
			dist[i][j] = graph[i][j];
		}
	}

	for(k = 0; k < n; k++){
	for(i = 0; i < n; i++){
	for(j = 0; j < n; j++){
		if ((graph[i][j] == -1 || graph[i][j] > (graph[i][k] + graph[k][j])) && (graph[k][j] != -1 && graph[i][k] != -1))
			dist[i][j] = dist[i][k] + dist[j][k];
	}}}

	printf("Floyd's Matrix: \n");
	for(i = 0; i < n; i++){
		for(j = 0; j < n; j++){
			if(dist[i][j] <= -1) printf("INF\t");
			else printf("%d\t", dist[i][j]);
		}
		printf("\n");
	}
}

void main(){
	// int n, graph[MAX][MAX]; scanf("%d", &n);
	// for(int i = 0; i < n; i++){
		// for(int j = 0; j < n; j++){
			// graph[i][j] = 999;
		// }
	// }
	// printf("Enter edges and dist, -1 to stop\n");
	// while(1){
		// int u, v, d; scanf("%d %d %d", &u, &v, &d);
		// if(u == -1) break;
		// graph[u][v] = d;
	// }
	int graph[MAX][MAX] = {
		{0, 4, -1, 5, -1},
		{-1, 0, 1, -1, 6},
		{2, -1, 0, 3, -1},
		{-1, -1, 1, 0, 2},
		{1, -1, -1, 4, 0}
	};	
	floyds(graph, 5);
}

// 0 4 5 5 7 
// 3 0 1 4 6 
// 2 6 0 3 5 
// 3 7 1 0 2 
// 1 5 5 4 0 
