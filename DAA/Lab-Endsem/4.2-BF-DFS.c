#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void dfs(int graph[MAX][MAX], int node, int n, int* visited){
  printf("Pushed: %d\n", node);
  visited[node] = 1;
  for(int i = 0; i < n; i++){
    if(graph[node][i] == 1 && visited[i] == 0){
      dfs(graph, i, n, visited);
    }
  }
  printf("Popped: %d\n", node);
}

void main(){
  int n = 4;
  int graph[MAX][MAX];
  while(1){
    int u, v;
    scanf("%d %d", &u, &v);
    if(u == -1) break;
    graph[u][v] = 1;
  }
  int visited[MAX];
  dfs(graph, 0, n, visited);
}