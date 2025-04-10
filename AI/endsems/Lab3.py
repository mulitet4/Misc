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
    
  def topo(self, node, visited=[], path=[]):
    visited.append(node)
    for nb in self.graph[node]:
      if nb not in visited:
        self.topo(nb, visited, path)
    path.append(node)
    return path

g = DAGraph()
g.add_edge([(5,2), (5,0), (4,0), (4,1), (2,3), (3,1)])
g.adj_list()
path: list = g.topo(5)
path.reverse()
print(path)

# Q2
class UDGraph:
  def __init__(self):
    self.graph = {}
  
  def add_edge(self, edges: list[tuple[int, int]]):
    for u, v in edges:
      if u not in self.graph:
        self.graph[u] = []
      if v not in self.graph:
        self.graph[v] = []
      self.graph[u].append(v)
  
  def check_cyclic(self, node, visited=[]):
    visited.append(node)
    is_cyclic = False
    for nb in self.graph[node]:
      if nb in visited:
        return True
      is_cyclic = self.check_cyclic(nb, visited)
    return False if not is_cyclic else True

g = UDGraph()
# g.add_edge([(0,2), (2,0), (1,2), (0, 1), (2,3), (3,3)])
g.add_edge([(2, 0), (0, 3), (3, 1)])
print(g.check_cyclic(2))