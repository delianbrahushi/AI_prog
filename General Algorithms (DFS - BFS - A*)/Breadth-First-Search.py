def BreadthFirstSearch(s):
    toDo = [[s]]

    while toDo:
        path = toDo.pop(0)  # FIFO
        current = path[-1]  # last node on the path so far

        if isGoal(current):
            return path

        for state in nextStates(current):
            state_not_in_path = state not in path

            state_not_in_toDo = True
            for p in toDo:
                if state in p:
                    state_not_in_toDo = False
                    break

            if state_not_in_path and state_not_in_toDo:
                toDo.append(path + [state]) 
                
    raise ValueError("FAILURE: NO PATH FOUND")
