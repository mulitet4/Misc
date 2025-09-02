import heapq

def ucs(graph, start, end):
  pq = []
  heapq.heappush(pq, (0, start))
  costs = {start: 0}
  parents = {start: None}
  while pq:
    cost_from_start, current_node = heapq.heappop(pq)
    if current_node == end:
      path = []
      while current_node != None:
        path.append(current_node)
        current_node = parents[current_node]
      path.reverse()
      return cost_from_start, path
    for neighbour, cost_to_neighbour in graph[current_node]:
      new_cost_from_start = cost_from_start + cost_to_neighbour
      if neighbour not in costs or new_cost_from_start < costs[neighbour]:
        costs[neighbour] = new_cost_from_start
        parents[neighbour] = current_node
        heapq.heappush(pq, (new_cost_from_start, neighbour))

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