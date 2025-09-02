#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

void Floyds(int graph[MAX][MAX], int n){
  int dist[n][n];
  for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
      dist[i][j] = graph[i][j];
    }
  }

  for(int k = 0; k < n; k++){
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
        if( (graph[i][j] == -1 || graph[i][j] < ( graph[i][k] + graph[k][j] )) && (graph[i][k] != -1 && graph[k][j] != -1) )
          dist[i][j] = dist[i][k] + dist[k][j];
      }
    }
  }

  printf("Floyd's Matrix: \n");
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
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
	Floyds(graph, 5);
}