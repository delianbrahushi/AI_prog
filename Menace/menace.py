import random

NUM_GUMDROPS = 10

def is_winner(state, player):
    # Check for winning conditions: rows, columns, diagonals
    win_indices = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                   (0, 4, 8), (2, 4, 6)]             # diagonals
    return any(all(state[i] == player for i in indices) for indices in win_indices)

def is_final_state(state):
    return is_winner(state, 'X') or is_winner(state, 'O') or '_' not in state

def make_move(state, move, player):
    new_state = list(state)
    new_state[move] = player
    return ''.join(new_state)

def choose(weights):
    total = sum(weights)
    roll = random.randint(1, total)
    for i in range(len(weights)):
        if roll <= weights[i]:
            return i
        roll -= weights[i]


def update_menace(menace, history, result):
    # result: 1 for MENACE win, -1 for MENACE loss, 0 for draw
    for state, move in history:
        if result == 1:  # Win
            menace[state][move] += 1
        elif result == -1 and menace[state][move] > 1:  # Loss
            menace[state][move] -= 1
        # No change for a draw


def OneGame(menace):
    state = "_________"
    history = []
    while not is_final_state(state):
        player = 'O' if state.count('X') > state.count('O') else 'X'
        if state not in menace:
            menace[state] = [NUM_GUMDROPS for _ in range(state.count('_'))]
        open_spots = [i for i, x in enumerate(state) if x == '_']
        if not open_spots:  # No more moves possible
            break
        chosen_index = choose(menace[state])
        move = open_spots[chosen_index]
        history.append((state, chosen_index))  # Store chosen index instead of move
        state = make_move(state, move, player)

    # Determine the result and update MENACE
    if is_winner(state, 'O'):  # Assuming MENACE plays 'O'
        update_menace(menace, history, 1 if player == 'O' else -1)
    elif is_winner(state, 'X'):
        update_menace(menace, history, -1 if player == 'O' else 1)
    else:
        update_menace(menace, history, 0)

    return history


# Train MENACE over a number of games
menace = {}
num_games = 10000
for _ in range(num_games):
    OneGame(menace)

# Print the trained MENACE dictionary
print("Trained MENACE Dictionary:")
for state, weights in sorted(menace.items()):
    print(f"{state}: {weights}")


