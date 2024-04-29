def AStarSearch(s, h):
    toDo = [[s]] 

    while toDo:
        toDo.sort(key=lambda path: h(path)) 
        path = toDo[0]
        toDo = toDo[1:]
        current = path[-1]  

        if isGoal(current):
            return path

        for state in nextStates(current):
            state_not_in_path = state not in path

            state_not_in_toDo = all(state not in p for p in toDo)

            if state_not_in_path and state_not_in_toDo:
                toDo.append(path + [state])  # append the extended path

    raise ValueError("FAILURE: NO PATH FOUND")

# Took the heuristic function from CS50 Artificial Intelligence with Python Course
def manhattan_distance(s, goal):
    return abs(s[0] - goal[0]) + abs(s[1] - goal[1])

def isGoal(s):
    return s == goal

def nextStates(s):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
    return [(s[0] + d[0], s[1] + d[1]) for d in dirs if allowed(s, d)]

def allowed(s, d):
    i, j = s[0] + d[0], s[1] + d[1]
    return 0 <= i < rows and 0 <= j < cols and grid[i][j] != 'W'

grid = [[' ', 'W', ' ', ' ', ' '],
        [' ', 'W', ' ', 'W', ' '],
        [' ', 'W', ' ', ' ', ' '],
        [' ', ' ', 'W', 'W', ' '],
        [' ', ' ', ' ', ' ', ' ']]

rows, cols = len(grid), len(grid[0])
start = (0, 0)
goal = (0, 4)

# empty places with the Manhattan distance values
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == ' ':
            grid[i][j] = str(manhattan_distance((i, j), goal))

try:
    path = AStarSearch(start, lambda path: manhattan_distance(path[-1], goal))
    print(path)

    #the final board with heuristics
    for row in grid:
        print(['\'{}\''.format(cell) if isinstance(cell, str) else cell for cell in row])

except ValueError as e:
    print(e)
