def AStarSearch(s, h):
    toDo = [[s]]

    while toDo:
        toDo.sort(key=lambda path: h(path))
        path = toDo[0]
        toDo = toDo[1:]
        current = path[-1]  # last node on the path so far

        if isGoal(current):
            return path

        for state in nextStates(current):
            state_not_in_path = state not in path

            state_not_in_toDo = all(state not in p for p in toDo)

            if state_not_in_path and state_not_in_toDo:
                toDo.append(path + [state])  # append the extended path

    raise ValueError("FAILURE: NO PATH FOUND")
