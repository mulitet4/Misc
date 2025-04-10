# Q1
class DAGraph:
  def __init__(self):
    self.graph = {}
  
  def add_edge(self, edges: list[tuple[int, int]]):
    for u, v in edges:
      if u not in self.graph:
        self.graph[u] = []
      if v not in self.graph:
        self.graph[v] = []
      self.graph[u].append(v)

  def adj_list(self):
    for node in sorted(self.graph):
      print(f"({node} -> {self.graph[node]})")
    
  def topo(self):
    q = []
    path = []
    indegree = {node: 0 for node in self.graph}
    for node in self.graph:
      for nb in self.graph[node]:
        indegree[nb] += 1
    
    for node in indegree:
      if indegree[node] == 0:
        q.append(node)
    
    while(q):
      node = q.pop(0)
      path.append(node)
      for nb in self.graph[node]:
        indegree[nb] -= 1
        if indegree[nb] == 0:
          q.append(nb)
    
    return path

  def is_cyclic(self):
    q = []
    visited = []
    q.append(sorted(self.graph)[0])
    while(q):
      node = q.pop(0)
      for nb in self.graph[node]:
        if nb in visited:
          return True
        q.append(nb)
    return False

g = DAGraph()
g.add_edge([(5,2), (5,0), (4,0), (4,1), (2,3), (3,1)])
path: list = g.topo()
print("Toposort: ", path)
print("Is DAG Cyclic: ", g.is_cyclic())

def tsp_bfs(graph, start):
  q = []
  q.append((start, [start], 0))
  min_path = None
  min_cost = float('inf')
  while q:
    current_city, path, cost = q.pop(0)
    if len(path) == len(graph) and start in graph[current_city]:
      total_cost = cost + graph[current_city][start]
      if total_cost < min_cost:
        min_cost = total_cost
        min_path = path + [start]
    
    for nb in graph[current_city]:
      if nb not in path:
        q.append((nb, path + [nb], cost + graph[current_city][nb]))
  return min_cost, min_path

graph = {
  'A': {'B': 2, 'C': 3, 'D': 1},
  'B': {'A': 2, 'C': 4, 'D': 2},
  'C': {'A': 3, 'B': 4, 'D': 3},
  'D': {'A': 1, 'B': 2, 'C': 3}
}

print("\nTSP Solution")
print(tsp_bfs(graph, 'C'))


def is_safe(state, row):
  for col in range(len(state)):
    if state[col] == row or abs(state[col] - row) == abs(len(state) - col):
      return False
  return True

def eight_queens_bfs(n):
  q = []
  q.append([])
  valid = []
  while(q):
    state = q.pop(0)
    if len(state) == n:
      return state
    for row in range(n):
      if is_safe(state, row):
        next_state = state + [row]
        q.append(next_state)
  return valid

print("\n8 Queens Solution")
print(eight_queens_bfs(8))


def bfs_water_jug(cap_a, cap_b, goal):
  visited = set()
  q = []
  q.append((0, 0))
  parents = {}
  while q:
    a, b = q.pop(0)
    if (a, b) in visited:
      continue
    visited.add((a,b))
    if a == goal or b == goal:
      path = []
      while (a, b) in parents:
        path.append((a,b))
        a, b = parents[(a,b)] 
      path.append((a,b))
      path.reverse()
      return path
    
    next_states = [
      (cap_a, b),
      (a, cap_b),
      (0, b),
      (a, 0),
      (a - min(a, cap_b - b), b + min(a, cap_b - b)),
      (a + min(cap_a - a, b), b - min(cap_a - a, b))
    ]

    for state in next_states:
      if state not in visited:
        parents[state] = (a,b)
        q.append(state)

bfs_result = bfs_water_jug(5, 3, 4)
print("\nWater Jug BFS:")
for step in bfs_result:
    print(step)


def get_nbs_8_puzzle(state):
  nbs = []
  idx = state.index(0)
  row, col = divmod(idx, 3)

  moves = {
    "up": -3,
    "down": 3,
    "left": -1,
    "right": 1
  }

  for move, delta in moves.items():
    new_idx = idx + delta
    if move == "left" and col == 0: continue
    if move == "right" and col == 2: continue
    if move == "up" and row == 0: continue
    if move == "down" and row == 2: continue
    if 0 <= new_idx <= 8:
      new_state = state[:]
      new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
      nbs.append(new_state)
  return nbs

def bfs_8_puzzle(start, goal):
  q = [(start, [])]
  visited = set()

  while q:
    current_state, path = q.pop(0)
    if current_state == goal:
      return path + current_state
    nbs = get_nbs_8_puzzle(current_state)
    for nb in nbs:
      if tuple(nb) not in visited:
        visited.add(tuple(nb))
        q.append((nb, path + [current_state]))

start_state = [1, 2, 3,
               4, 0, 5,
               6, 7, 8]

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

path = bfs_8_puzzle(start_state, goal_state)
print("\nBFS 8 Puzzle:")
print(path)

# Toposort:  [5, 4, 2, 0, 3, 1]
# Is DAG Cyclic:  False

# TSP Solution
# (10, ['C', 'A', 'B', 'D', 'C'])      

# 8 Queens Solution
# [0, 4, 7, 5, 2, 6, 1, 3]

# Water Jug BFS:
# (0, 0)
# (5, 0)
# (2, 3)
# (2, 0)
# (0, 2)
# (5, 2)
# (4, 3)