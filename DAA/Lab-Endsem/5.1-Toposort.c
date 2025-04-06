#include <stdio.h>
#include <stdlib.h>
#define MAX 100

void dfsTopo(int graph[MAX][MAX], int node, int n, int* visited){
  visited[node] = 1;
  for(int i = 0; i < n; i++){
    if(graph[node][i] == 1 && visited[i] == 0){
      dfsTopo(graph, i, n, visited);
    }
  }
  printf("%d\t", node);
}

void srcRemTopo(int graph[MAX][MAX], int n){
  int q[MAX];
  int front = 0, rear = -1;
  int indegree[MAX] = {0};
  for(int i = 0; i < n; i++){ 
    for(int j = 0; j < n; j++){
      if(graph[i][j] == 1) indegree[j]++;
    }
  }
  for(int i = 0; i < n; i++){
    if(indegree[i] == 0) q[++rear] = i;
  }
  while(front <= rear){
    int node = q[front++];
    printf("%d ", node);
    for(int i = 0; i < n; i++){
      if(graph[node][i] == 1){
        indegree[i]--;
        graph[node][i] = 0;
        if(indegree[i] == 0){
          q[++rear] = i;
        }
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
  dfsTopo(graph, 0, n, visited); printf("\n");
  srcRemTopo(graph, n);
}