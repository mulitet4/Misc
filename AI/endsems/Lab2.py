# Q1
class UDGraph:
  def __init__(self):
    self.graph = {}
  
  def add_edge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    if v not in self.graph:
      self.graph[v] = []
    self.graph[u].append(v)
  
  def adj_list(self):
    for node in sorted(self.graph):
      print(f"({node} -> {self.graph[node]})")

g = UDGraph()
g.add_edge(5, 4)
g.add_edge(4, 5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.add_edge(3, 2)
g.adj_list()

# Q2
class UndWeiGraph:
  def __init__(self):
    self.graph = {}
  
  def add_edge(self, u, v, w):
    if u not in self.graph:
      self.graph[u] = {}
    if v not in self.graph:
      self.graph[v] = {}
    self.graph[u][v] = w
  
  def adj_list(self):
    for node in sorted(self.graph):
      print(f"({node} -> {self.graph[node]})")

g = UndWeiGraph()
g.add_edge(0,1,6)
g.add_edge(1,2,7)
g.add_edge(2,0,5)
g.add_edge(2,1,4)
g.add_edge(3,2,10)
g.add_edge(4,5,1)
g.add_edge(5,4,3)
g.adj_list()