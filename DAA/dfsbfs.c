#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int graph[100][100];
  int nodes;
} G;

void dfs(G* g, int start, int visited[100]){
  visited[start] = 1;
  printf("%d ", start);
  for(int neighbour = 0; neighbour < g->nodes; neighbour++){
    if(g->graph[start][neighbour] == 1 && visited[neighbour] == 0){
      dfs(g, neighbour, visited);
    }
  }
}

int bfs(G* g, int start){
  int visited[100] = {0};
  int q[100], f = 0, r = -1;
  q[++r] = start;
  while(f <= r){
    int node = q[f++];
    printf("%d ", node);
    for(int neighbour = 0; neighbour < g->nodes; neighbour++){
      if(g->graph[node][neighbour] == 1 && visited[neighbour] != 1){
        visited[neighbour] = 1;
        q[++r] = neighbour;
      }
    }
  }
}

void addEdge(G* g, int u, int v){
  g->graph[u][v] = 1;
}

void main(){
  G* g = (G*) malloc(sizeof(G));
  g->nodes = 5;
  addEdge(g, 5, 0);
  addEdge(g, 5, 3);
  addEdge(g, 3, 2);
  addEdge(g, 2, 1);
  addEdge(g, 4, 1);
  addEdge(g, 4, 0);
  int visited[100] = {0};
  dfs(g, 5, visited);
  printf("\n");
  bfs(g, 5);
}