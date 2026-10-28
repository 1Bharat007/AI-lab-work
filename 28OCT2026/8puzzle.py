
import time
from math import inf

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

State = tuple[int, ...]


# 1. Heuristic: count misplaced tiles
def misplaced_tiles(state: State) -> int:
    count = 0

    for i, tile in enumerate(state):
        if tile != 0 and tile != GOAL[i]:
            count += 1

    return count


# 2. Heuristic: Manhattan distance
def manhattan_distance(state: State) -> int:
    distance = 0

    for i, tile in enumerate(state):
        if tile == 0:
            continue

        current_row, current_col = divmod(i, 3)

        goal_index = tile - 1
        goal_row, goal_col = divmod(goal_index, 3)

        distance += (
            abs(current_row - goal_row)
            + abs(current_col - goal_col)
        )

    return distance


# 3. Check whether the puzzle is solvable
def is_solvable(state: State) -> bool:
    numbers = [tile for tile in state if tile != 0]
    inversions = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1

    # For a standard 3 x 3 puzzle, even inversions
    # means the board is solvable.
    return inversions % 2 == 0


# 4. Generate all valid neighboring boards
def get_neighbors(state: State):
    blank = state.index(0)
    row, col = divmod(blank, 3)

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank = new_row * 3 + new_col

            board = list(state)
            board[blank], board[new_blank] = (
                board[new_blank], board[blank]
            )

            yield tuple(board)


# 5. Reconstruct the solution path
def reconstruct_path(parent, goal_state):
    path = []
    current = goal_state

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path


# 6. A* search WITHOUT a priority queue
def astar(start: State, heuristic):
    if len(start) != 9 or sorted(start) != list(range(9)):
        raise ValueError(
            "Board must contain each number from 0 to 8 exactly once."
        )

    if not is_solvable(start):
        return None, 0

    # Frontier entries: (f, h, g, state)
    frontier = [
        (heuristic(start), heuristic(start), 0, start)
    ]

    # Best known cost from start to each state
    g_score = {start: 0}

    # Parent of each state, used to reconstruct the path
    parent = {start: None}

    # Best cost at which each state has been expanded
    expanded_g = {}

    expanded_nodes = 0

    while frontier:

        # Find the entry with minimum f, then minimum h.
        # This is a normal list scan, not a priority queue.
        best_index = min(
            range(len(frontier)),
            key=lambda i: (frontier[i][0], frontier[i][1])
        )

        f, h, g, current = frontier.pop(best_index)

        # Ignore an outdated entry
        if g != g_score.get(current):
            continue

        # Avoid expanding the same state at the same
        # or a worse path cost.
        if current in expanded_g and expanded_g[current] <= g:
            continue

        expanded_g[current] = g

        # The goal has been reached
        if current == GOAL:
            path = reconstruct_path(parent, current)
            return path, expanded_nodes

        expanded_nodes += 1

        for neighbor in get_neighbors(current):
            tentative_g = g + 1

            # Update only if this route is better
            if tentative_g < g_score.get(neighbor, inf):
                g_score[neighbor] = tentative_g
                parent[neighbor] = current

                h_neighbor = heuristic(neighbor)
                f_neighbor = tentative_g + h_neighbor

                frontier.append(
                    (f_neighbor, h_neighbor, tentative_g, neighbor)
                )

    return None, expanded_nodes


# 7. Display a board
def print_board(state: State):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join("_" if x == 0 else str(x) for x in row))
    print()


# 8. Compare the two heuristics
def compare_heuristics(start: State):
    heuristics = [
        ("Misplaced Tiles", misplaced_tiles),
        ("Manhattan Distance", manhattan_distance)
    ]

    for name, heuristic in heuristics:
        begin = time.perf_counter()

        path, expanded = astar(start, heuristic)

        elapsed = time.perf_counter() - begin

        print("=" * 40)
        print(name)

        if path is None:
            print("No solution exists for this board.")
            print("Expanded nodes:", expanded)
            continue

        print("Solution length:", len(path) - 1, "moves")
        print("Expanded nodes:", expanded)
        print(f"Execution time: {elapsed:.6f} seconds")

        print("\nSolution path:")
        for step, state in enumerate(path):
            print(f"Step {step}:")
            print_board(state)


# 9. Run the program
if __name__ == "__main__":
    start_state = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    )

    compare_heuristics(start_state)
