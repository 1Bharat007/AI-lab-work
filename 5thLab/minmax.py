# LAB 05: Minimax for Tic-Tac-Toe

board = [" "] * 9

wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def winner(player):
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in wins
    )

def minimax(is_max):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    if is_max:
        best = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    best = float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(True)
            board[i] = " "
            best = min(best, score)

    return best

def best_move():
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move

board[best_move()] = "O"

for i in range(0, 9, 3):
    print(" | ".join(board[i:i+3]))
    if i < 6:
        print("---------")