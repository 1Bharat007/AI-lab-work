import heapq

def greedy_best_first_search(graph , heuristic , start , goal ) :
    queue =[(heuristic[start] , start)]
    parent = {start: None} 
    visited = set()

    while queue:
        node = heapq.heappop(queue)

        if node in visited :
            continue
            visited.add(node)

        if node == goal:
            path=[]
            while node is not None:
                path.append(node)
                node = parent[node]
            return list(reversed(path))

        for neighbor, _ in graph[node]:
            if neighbour not in visited:

                parent[neighbor] = node
                heapq.heappush(queue , (heuristic[neighbor], neighbour))

return None


graph = {
    "S" : [("A" , 2) , ("B" , 1)] ,
    "A" : [("G" , 2) , ("Y" , 7)] ,
    "B" : [("U" , 4) , ("T" , 8)],
    "G" : [] ,
}


print(type(graph)) 

heuristic = {"S" : 0 , "A" , 2  , "B" : 1 , "G" : 0}

print(greedy_best_first_search(graph , heuristic , "S" , "G"))

