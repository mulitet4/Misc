#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void bfs(int graph[MAX][MAX], int node, int n){
  int q[MAX] = {0}, visited[MAX] = {0};
  int front = 0, rear = -1;
  q[++rear] = node;

  while(front <= rear){
    int node = q[front++];
    visited[node] = 1;
    printf("Visited: %d\n", node);
    for(int i = 0; i < n; i++){
      if(graph[node][i] == 1 && visited[i] == 0){
        q[++rear] = i;
      }
    }
  }
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
  bfs(graph, 0, n);
}