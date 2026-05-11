import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('C', 1), ('D', 7)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

def dijkstra(start):

    distances = {}

    for vertex in graph:
        distances[vertex] = float('inf')

    distances[start] = 0

    heap = [(0, start)]

    while heap:

        current_distance, current_vertex = heapq.heappop(heap)

        for neighbor, weight in graph[current_vertex]:

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(heap,
                               (distance, neighbor))

    return distances

print(dijkstra('A'))