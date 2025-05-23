import math

# Initialize board
board = [" " for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in win_conditions)

def is_full():
    return " " not in board

def minimax(state, depth, is_maximizing):
    if winner(state, "O"):
        return 1
    elif winner(state, "X"):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in available_moves():
            state[i] = "O"
            score = minimax(state, depth + 1, False)
            state[i] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in available_moves():
            state[i] = "X"
            score = minimax(state, depth + 1, True)
            state[i] = " "
            best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    board[move] = "O"

def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"
        print_board()

        if winner(board, "X"):
            print("You win!")
            break
        if is_full():
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        ai_move()
        print_board()

        if winner(board, "O"):
            print("AI wins!")
            break
        if is_full():
            print("It's a tie!")
            break

# Run the game
play_game()
