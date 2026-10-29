# LAB 04C: Tic-Tac-Toe basic search

board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def move():
    for i in range(9):
        if board[i] == " ":
            return i

show()

position = move()
board[position] = "X"

print("\nAfter choosing a move:")
show()