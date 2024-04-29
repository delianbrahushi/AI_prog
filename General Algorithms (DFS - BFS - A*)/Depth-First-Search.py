def depth_first_search(s):
    to_do = [[s]]

    while to_do:
        path = to_do.pop()  # LIFO
        current = path[-1]  

        if is_goal(current):
            return path  

        for state in next_states(current):
            state_not_in_path = state not in path
            state_not_in_to_do = all(state not in p for p in to_do)

            if state_not_in_path and state_not_in_to_do:
                to_do.append(path + [state])  # Push the new path

    raise ValueError("FAILURE: NO PATH FOUND")
