def dfs(graph, start, visited = [], result = []):
  result.append(start)
  for neighbour in graph[start]:
    if neighbour in visited:
      continue
    visited.append(neighbour)
    dfs(graph, neighbour, visited, result)
  return result

def dfs_topo(graph):
  visited = set()
  result = []
  def dfs(node):
    visited.add(node)
    for neighbour in graph[node]:
      if neighbour in visited:
        continue
      dfs(neighbour)
    result.append(node)

  for node in graph:
    if node not in visited:
      dfs(node)
  result.reverse()
  return result

def detect_cycle(graph, start, visited = []):
  visited.append(start)
  result = False
  for neighbour in graph[start]:
    if neighbour in visited:
      return True
    result = detect_cycle(graph, neighbour, visited)
  return result

def maze_solve(graph, start, end, visited = [], result = []):
  visited.append(start)
  result.append(start)
  for neighbour in graph[start]:
    if neighbour == end:
      print(result)
      return
    if neighbour in visited:
      continue
    maze_solve(graph, neighbour, end, visited, result)
  result.pop(-1)

def is_bi(graph):
  n = len(graph)
  color = [-1] * n
  
  def dfs(node, c):
    color[node] = c
    for neighbour in graph[node]:
      if color[neighbour] == -1:
        if not dfs(neighbour, c):
          return False
      elif color[neighbour] == color[node]:
        return False
    return True
  
  for i in range(i):
    if color[i] == -1:
      if not dfs(i, 0):
        return False
  return True

print(dfs({5: [0, 2], 4: [0, 1], 2: [3], 3: [1], 0: [], 1:[]}, 5))
print(dfs_topo({5: [0, 2], 4: [0, 1], 2: [3], 3: [1], 0: [], 1:[]}))
print(detect_cycle({2: [0, 3], 0: [2, 1], 1: [2], 3: [3]}, 2))
maze_solve({
    1: [2, 6],
    2: [1, 3],
    3: [2, 8],
    4: [5],
    5: [4, 10],
    6: [1, 11],
    7: [8],
    8: [7, 3],
    9: [14, 10],
    10: [5, 9, 15],
    11: [6, 12],
    12: [11, 17],
    13: [14],
    14: [9, 13, 19],
    15: [10, 20],
    16: [17],
    17: [12, 16, 18],
    18: [17, 19],
    19: [14, 18],
    20: [15]
}, 2, 5)