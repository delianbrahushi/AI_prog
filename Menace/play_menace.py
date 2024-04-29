import random
from menace import choose, is_winner, is_final_state, make_move , OneGame

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

def human_move(state):
    print_board(state)
    move = -1
    while move < 0 or move > 8 or state[move] != '_':
        try:
            move = int(input("Enter your move (0-8): "))
            if state[move] != '_':
                print("Illegal move, try again.")
        except ValueError:
            print("Invalid input, please enter a number between 0 and 8.")
    return move


def menace_move(state, menace):
    player = 'O' if state.count('X') > state.count('O') else 'X'
    if state not in menace:
        # If the state is not in the dictionary, return a random move
        return random.choice([i for i, x in enumerate(state) if x == '_'])

    # Use the trained weights to choose a move
    open_spots = [i for i, x in enumerate(state) if x == '_']
    if not open_spots:  # No more moves possible
        return None

    # Choose a move based on the weights in the MENACE dictionary
    chosen_index = choose(menace[state])
    return open_spots[chosen_index]

def play_with_menace(menace):
    state = "_________"
    while not is_final_state(state):
        if state.count('X') <= state.count('O'):
            move = human_move(state)
            player = 'X'
        else:
            move = menace_move(state, menace)
            player = 'O'
        state = make_move(state, move, player)
        print_board(state)

        if is_winner(state, 'O'):
            print("O wins!")
            break
        elif is_winner(state, 'X'):
            print("X wins!")
            break

    if not is_winner(state, 'X') and not is_winner(state, 'O'):
        print("It's a draw!")


if __name__ == "__main__":
    menace_dictionary = {}  # Create the MENACE dictionary

    # Train MENACE
    num_games = 10000
    for _ in range(num_games):
        OneGame(menace_dictionary)

    # Now play with the trained MENACE
    play_with_menace(menace_dictionary)
