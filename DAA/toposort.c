#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct g {
  int graph[MAX][MAX];
  int nodes;
} G;

void addEdge(G* g, int u, int v){
  g->graph[u][v] = 1;
}

void dfstoporec(G* g, int start, int visited[MAX], int* sorted, int* s_top){
  visited[start] = 1;
  for(int i = 0; i < g->nodes; i++){
    if(g->graph[start][i] == 1 && visited[i] != 1){
      dfstoporec(g, i, visited, sorted, s_top);
    }
  }
  sorted[++(*s_top)] = start;
}

void dfssrcremoval(G* g, int* sorted, int* s_top){
  // number of 1s in the colum will give indegree
  int indegree[MAX] = {0};
  for(int i = 0; i < g->nodes; i++){
    for(int j = 0; j < g->nodes; j++){
      if(g->graph[j][i]) indegree[i]++ ;
    }
  }
  
  int q[MAX], f = 0, r = -1;
  for(int i = 0; i < g->nodes; i++){
    if(indegree[i] == 0){
      q[++r] = i;
    }
  }

  while(f <= r){
    int node = q[f++];
    sorted[++(*s_top)] = node;
    for(int i = 0; i < g->nodes; i++){
      if(g->graph[node][i]){
        indegree[i]--;
        if(indegree[i] == 0){
          q[++r] = i;
        }
      }
    }
  }
  printf("\n");

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
  int sorted[MAX];
  int s_top = -1;
  int visited[MAX];
  dfstoporec(g, 5, visited, sorted, &s_top);
  for (int i = s_top; i >= 0; i--) {
    printf("%d ", sorted[i]);
  }
  int sorted2[MAX];
  int s_top2 = -1;
  printf("\n");

  dfssrcremoval(g, sorted2, &s_top2);
  for (int i = 0; i <= s_top2; i++) {
    printf("%d ", sorted2[i]);
  }
}