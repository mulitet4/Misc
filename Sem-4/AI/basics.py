class Stack:
  def __init__(self):
    self.a = []
    self.b = []
  
  def enq(self, item):
    self.a.append(item)

  def deq(self):
    if not self.b:
      while self.a:
        self.b.append(self.a.pop())
    
    return self.b.pop()

class WDGraph:
  def __init__(self):
    self.graph: dict[int, list[tuple[int, int]]] = {}
  
  def add_edge(self, edges):
    for u, v, w in edges:
      if u not in self.graph:
        self.graph[u] = []
      if v not in self.graph:
        self.graph[v] = []
      self.graph[u].append((v, w))
  
  def adj_list(self):
    for node in self.graph:
      print(node, self.graph[node])
  
  def adj_mat(self):
    nodes = sorted(self.graph)
    adj_mat = [[0] * len(nodes) for _ in nodes]

    for node in nodes:
      for v, w in self.graph[node]:
        adj_mat[node][v] = w
    
    for row in adj_mat:
      for col in row:
        print(col, end=' ')
      print()

class Node:
  def __init__(self, data):
    self.data = data
    self.l = None
    self.r = None

class Tree:
  def __init__(self, root):
    self.root = Node(root)

  def insert(self, data):
    n = Node(data)
    temp = self.root
    par = None
    while temp:
      par = temp
      if(data < temp.data):
        temp = temp.l
      elif(data > temp.data):
        temp = temp.r
      else:
        print("Duplicate")
        return
    if data < par.data:
      par.l = n
    else:
      par.r = n
  
  def inorder(self):
    def inorder_rec(node: Node):
      if node:
        inorder_rec(node.l)
        print(node.data, end=' ')
        inorder_rec(node.r)
    inorder_rec(self.root)

s = Stack()
s.enq(1)
s.enq(2)
print(s.deq())
print(s.deq())

g = WDGraph()
g.add_edge([(1, 2, 1), (1,3,1), (2,3,3), (3,4,4), (4,1,5)])
g.adj_list()

t = Tree(25)
t.insert(15)
t.insert(10)
t.insert(22)
t.inorder()