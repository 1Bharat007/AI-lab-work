from collections import deque

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            board = list(state)

            board[zero], board[pos] = board[pos], board[zero]

            yield tuple(board)


def bfs():
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution found!")

            for board in path:
                print(board[:3])
                print(board[3:6])
                print(board[6:])
                print()

            return

        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    print("No solution found")


bfs()
