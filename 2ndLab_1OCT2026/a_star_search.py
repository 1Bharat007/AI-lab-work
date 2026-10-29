# LAB 02B: A* Search

import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 2)],
    'D': [], 'E': [('G', 1)],
    'F': [('G', 3)], 'G': []
}

h = {
    'A': 5, 'B': 4, 'C': 4, 'D': 2,
    'E': 1, 'F': 3, 'G': 0
}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    best_cost = {start: 0}

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            return path, g

        if g > best_cost[node]:
            continue

        for neighbor, cost in graph[node]:
            new_g = g + cost

            if new_g < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_g

                heapq.heappush(
                    queue,
                    (new_g + h[neighbor], new_g,
                     neighbor, path + [neighbor])
                )

    return None, float('inf')

path, cost = astar('A', 'G')
print("Path:", path)
print("Cost:", cost)