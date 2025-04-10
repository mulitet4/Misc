# Any random function
import random

def f(x):
  return -x**2 + 5

def get_neighbours(x):
  return [x-0.5, x+0.5]

def hill_climb(start_x):
  current_x = start_x
  current_val = f(start_x)
  print(current_x, current_val)

  while True:
    nb = get_neighbours(current_x)
    nb = [n for n in nb if -10 <- n <= 10]
    nb_val = [(n, f(n)) for n in nb]

    best_nb = max(nb_val, key=lambda x: x[1])
    if best_nb[1] > current_val:
      current_x = best_nb[0]
      current_val = best_nb[1]
      print(current_x, current_val)
    else:
      break
  
  print(f"Max at x = {current_x}, f(x) = {current_val}")

print("\nHill Climbing f(x):")
start = random.randint(-10, 10)
hill_climb(start)


# 8 Queens
def random_state():
  return [random.randint(0, 7) for _ in range(8)]

def conflicts(state: list):
  conflicts = 0
  for i in range(len(state)):
    for j in range(i+1, len(state)):
      if(state[i] == state[j]):
        conflicts += 1
      if abs(state[i] - state[j]) == abs(i - j):
        conflicts += 1
  return conflicts

def get_board_nbs(state: list, visited: list):
  neighbours = []
  for col in range(len(state)):
    for row in range(len(state)):
      if row != state[col]:
        new_state = state[:]
        new_state[col] = row
        if new_state not in visited:
          visited.append(new_state)
          neighbours.append(new_state)
  return neighbours

def hill_climb_8_queens():
  current_state = random_state()
  current_conflicts = conflicts(current_state)
  visited = []

  while True:
    nbs = get_board_nbs(current_state, visited)
    nbs_conflicts = [(n, conflicts(n)) for n in nbs]
    best_nb = min(nbs_conflicts, key=lambda x: x[1])

    if current_conflicts != 0:
      current_state, current_conflicts = best_nb
      print(current_state, current_conflicts)
    else:
      break
  
  if current_conflicts == 0:
    print("Solution found: ", current_state)
  else:
    print("Solution not found")

print("\nHill Climbing 8 Queens:")
hill_climb_8_queens()


# Water jug problem
def h(a, b, goal):
  return abs(a - goal) + abs(b - goal)

def hill_climb_water_jug(cap_a, cap_b, goal):
  current_state = (0, 0)
  visited = set()
  path = [current_state]

  while True:
    a, b = current_state

    neighbours = [
      (a, cap_b),
      (cap_a, b),
      (a, 0),
      (0, b),
      (a - min(a, cap_b - b), b + min(a, cap_b - b)),
      (a + min(cap_a - a, b), b - min(cap_a - a, b))
    ]
    nb_vals = [(n, h(n[0], n[1], goal)) for n in neighbours if n not in visited]
    best_nb = min(nb_vals, key=lambda x: x[1])

    if a != goal and b != goal:
      visited.add(current_state)
      path.append(current_state)
      current_state = best_nb[0]
    else:
      return path
    
hc_result = hill_climb_water_jug(10, 7, 4)
print("\nHill Climbing Water Jug:")
for step in hc_result:
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

  for move, dx in moves.items():
    new_idx = idx + dx
    if move == "up" and row == 0: continue
    if move == "down" and row == 2: continue
    if move == "left" and col == 0: continue
    if move == "right" and col == 2: continue
    if 0 <= new_idx <= 8:
      new_state = state[:]
      new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
      nbs.append(new_state)
  return nbs

def h_8_puzzle(state, goal):
    return sum([1 for i in range(9) if state[i] != 0 and state[i] != goal[i]])

def hill_climb(start, goal):
    current = start[:]
    path = [current]
    visited = []

    while True:
        neighbors = get_nbs_8_puzzle(current)
        nb_val = [(n, h_8_puzzle(n, goal)) for n in neighbors if n not in visited]
        best_nb = min(nb_val, key=lambda x: x[1])

        if goal != current:
          current = best_nb[0]
          path.append(best_nb[0])
          visited.append(best_nb[0])
        else:
          break

    return path

start_state = [1, 2, 3,
               4, 0, 5,
               6, 7, 8]

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

hc_path = hill_climb(start_state, goal_state)
print("\nHill Climbing 8 Puzzle:")
for step in hc_path:
    print(step)

# Hill Climbing f(x):
# -1 4
# -0.5 4.75
# 0.0 5.0
# Max at x = 0.0, f(x) = 5.0

# Hill Climbing 8 Queens:
# [7, 7, 3, 1, 2, 4, 6, 4] 3
# [0, 7, 3, 1, 2, 4, 6, 4] 3
# [0, 7, 5, 1, 2, 4, 6, 4] 3
# [0, 7, 5, 1, 2, 4, 6, 3] 2
# [1, 7, 5, 1, 2, 4, 6, 3] 2
# [1, 7, 5, 0, 2, 4, 6, 3] 0
# Solution found:  [1, 7, 5, 0, 2, 4, 6, 3]

# Hill Climbing Water Jug:
# (0, 0)
# (0, 7)
# (7, 0)
# (7, 7)
# (10, 4)