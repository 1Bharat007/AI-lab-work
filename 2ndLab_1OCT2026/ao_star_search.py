# LAB 02C: AO* Search (simple AND-OR graph example)

graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E']],
    'C': [['F']],
    'D': [['G']],
    'E': [], 'F': [], 'G': []
}

cost = {
    'A': 1, 'B': 2, 'C': 2, 'D': 4,
    'E': 1, 'F': 3, 'G': 1
}

def ao_star(node):
    if not graph[node]:
        return cost[node]

    best = float('inf')

    for option in graph[node]:
        total = cost[node]

        for child in option:
            total += ao_star(child)

        best = min(best, total)

    return best

print("Minimum cost:", ao_star('A'))