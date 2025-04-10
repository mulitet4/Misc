def pop_least(pq):
  min = float('inf')
  min_i = 0
  for i, pair in enumerate(pq):
    if pair[1] < min:
      min = pair[1]
      min_i = i
  return pq.pop(min_i)

def ucs(graph, start, goal):
  pq = []
  pq.append((start, 0))
  costs = {start: 0}
  parents = {start: None}
  while pq:
    node, cost_to_node = pop_least(pq)
    if node == goal:
      path = []
      while node:
        path.append(node)
        node = parents[node]
      path.reverse()
      return cost_to_node, path
    for nb, cost in graph[node]:
      cost_to_nb = cost_to_node + cost
      if nb not in costs or cost_to_nb < costs[nb]:
        costs[nb] = cost_to_nb
        parents[nb] = node
        pq.append((nb, cost_to_nb))

graph = {
    'S': [('1', 2), ('3', 5)],
    '1': [('G', 1)],
    '2': [('1', 4)],
    '3': [('1', 5),('G', 6)],
    '4': [('2', 4)],
    '5': [('G', 3), ('2', 6)],
} 

start = 'S'
goal = 'G'
cost, path = ucs(graph, start, goal)
print(f"The cheapest cost from {start} to {goal} is: {cost} & path is {path}")