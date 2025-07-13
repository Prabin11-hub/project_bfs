import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start, [start]))

    while priority_queue:
        h_cost, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            print('Path found:', path)
            return

        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    print('No path found')

#These should NOT be indented — define them outside any function
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 12)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 2)],
    'F': [('E', 1)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 1,
    'F': 4,
    'G': 0
}

# Run the function
best_first_search(graph, 'A', 'G', heuristic)