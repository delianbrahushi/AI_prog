from PIL import Image, ImageDraw


def BreadthFirstSearch(s, grid, rows, cols):
    toDo = [[s]]  # initialize a list of paths to explore

    while toDo:
        path = toDo.pop(0)  # dequeue the first path for exploration
        current = path[-1]  # last node on the path so far

        if isGoal(current, grid):
            return path

        for state in nextStates(current, grid, rows, cols):
            state_not_in_path = state not in path

            state_not_in_toDo = True
            for p in toDo:
                if state in p:
                    state_not_in_toDo = False
                    break

            if state_not_in_path and state_not_in_toDo:
                toDo.append(path + [state])  # enqueue the extended path

    raise ValueError("FAILURE: NO PATH FOUND")


def isGoal(s, grid):
    return grid[s[0]][s[1]] == 'G'


def nextStates(s, grid, rows, cols):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
    return [(s[0] + d[0], s[1] + d[1]) for d in dirs if allowed(s, d, grid, rows, cols)]


def allowed(s, d, grid, rows, cols):
    i, j = s[0] + d[0], s[1] + d[1]
    return 0 <= i < rows and 0 <= j < cols and grid[i][j] != 'W'


def output_image(filename, grid, start, path=None):
    cell_size = 50
    cell_border = 2

    # Find the position of the goal in the grid
    goal = None
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 'G':
                goal = (i, j)
                break
        if goal:
            break

    if goal is None:
        raise ValueError("Goal not found in the maze.")

    # Create a blank canvas
    img = Image.new(
        "RGBA",
        (len(grid[0]) * cell_size, len(grid) * cell_size),
        "black"
    )
    draw = ImageDraw.Draw(img)

    for i, row in enumerate(grid):
        for j, col in enumerate(row):

            # Walls
            if col == 'W':
                fill = (40, 40, 40)

            # Start
            elif (i, j) == start:
                fill = (255, 0, 0)

            # Goal
            elif (i, j) == goal:
                fill = (0, 171, 28)

            # Path
            elif path is not None and (i, j) in path:
                fill = (220, 235, 113)

            # Empty cell
            else:
                fill = (237, 240, 252)

            # Draw cell
            draw.rectangle(
                ([(j * cell_size + cell_border, i * cell_size + cell_border),
                  ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                fill=fill
            )

    img.save(filename)



grid = [
    ['W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', 'W', 'W', 'W',
     'W', 'W', 'W', 'W', 'W', 'W']
    ,
    ['W', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     ' ', ' ', ' ', 'W', ' ', 'W'],
    ['W', ' ', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', ' ', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', ' ', 'W', ' ', 'W', 'W', ' ', 'W', 'W', 'W', ' ', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', ' ', 'W', ' ', ' ', ' ', ' ', 'W', ' ', ' ', ' ', 'W', 'W', ' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', ' ', 'W', ' ', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', 'W', 'W', ' ', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', ' ', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', ' ', ' ', ' ', ' ', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     ' ', 'W', ' ', 'W', ' ', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W', 'W', 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
     ' ', 'W', ' ', ' ', ' ', 'W'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     'W', 'W', 'W', 'W', 'W', 'W']]

rows, cols = len(grid), len(grid[0])
start = (15, 0) # ARBITRARY START (based on provided grid)
try:
    path = BreadthFirstSearch(start, grid, rows, cols)

    # Output image
    output_image('maze_solution.png', grid, start, path)
    print("Path to goal:", path)
except ValueError as e:
    print(e)
