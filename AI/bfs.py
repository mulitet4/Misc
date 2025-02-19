def bfs(graph, start):
  q = []
  result = []
  q.append(start)
  while q:
    node = q.pop(0)
    result.append(node)
    for neighbour in graph[node]:
      q.append(neighbour)
  
  print(result)

def bfs_topo(graph: dict[int, list[int]], start):
  indegree = {node: 0 for node in graph.keys()}
  for node, neighbours in graph.items():
    for neighbour in neighbours:
      indegree[neighbour] = indegree[neighbour] + 1
        
  q = []
  result = []
  for node, count in indegree.items():
    if count == 0:
      q.append(node)
  
  while q:
    node = q.pop(0)
    result.append(node)
    for neighbour in graph[node]:
      indegree[neighbour] = indegree[neighbour] - 1
      if indegree[neighbour] == 0:
        q.append(neighbour)

  print(result)

def check_cyclic(graph, start):
  visited = set()
  q = []
  q.append(start)
  while q:
    node = q.pop(0)
    visited.add(node)
    for neighbour in graph[node]:
      if neighbour in visited:
        return True
      q.append(neighbour)
  return False

bfs({5: [0, 2], 4: [0, 1], 2: [3], 3: [1], 0: [], 1:[]}, 5)
bfs_topo({5: [0, 2], 4: [0, 1], 2: [3], 3: [1], 0: [], 1:[]}, 5)
print(check_cyclic({2: [0, 3], 0: [2, 1], 1: [2], 3: [3]}, 2))