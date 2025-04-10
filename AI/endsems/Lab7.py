def remove_least(pq):
  min = float('inf')
  i = -1
  for ind, (f_cost, node) in enumerate(pq):
    if f_cost < min:
      min = f_cost
      i = ind
  return pq.pop(i)

def astar(graph, start, hmap, goal):
  pq = []
  costs = {start: 0 + hmap[start]}
  parents = {start: None}
  pq.append((0 + hmap[start], start))
  while pq:
    f_cost, node = remove_least(pq)
    if node == goal:
      path = []
      while node:
        path.append(node)
        node = parents[node]
      path.reverse()
      return f_cost, path
    for nb in graph[node]:
      f_cost_to_nb = f_cost + graph[node][nb] + hmap[nb]
      if nb not in costs or f_cost_to_nb < costs[nb]:
        costs[nb] = f_cost_to_nb
        parents[nb] = node
        pq.append((f_cost_to_nb, nb))

print(astar({
    'A': {'B': 6, 'F': 3},
    'B': {'C': 3, 'D': 2, 'A': 6},
    'C': {'B': 3, 'D': 1, 'E': 5},
    'D': {'B': 2, 'C': 1, 'E': 8},
    'E': {'C': 5, 'D': 8, 'I': 5, 'J': 5},
    'F': {'G': 1, 'H': 7, 'A': 3},
    'G': {'F': 1, 'I': 3},
    'H': {'F': 7, 'I': 2},
    'I': {'G': 3, 'H': 2, 'J': 3, 'E': 5},
    'J': {'I': 3, 'E': 5}
}, 'A', {
    'A': 10, 'B': 8, 'C': 5, 
    'D': 7, 'E': 3, 'F': 6, 
    'G': 5, 'H': 3, 'I': 1, 
    'J': 0
 }, 'J'))
