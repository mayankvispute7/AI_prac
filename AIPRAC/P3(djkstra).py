import heapq

# Create graph dictionary
graph = {}

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Input vertex names
vertices = []

print("\nEnter vertex names:")

for i in range(n):
    vertex = input(f"Vertex {i+1}: ")
    vertices.append(vertex)
    graph[vertex] = []

# Input number of edges
e = int(input("\nEnter number of edges: "))

print("\nEnter edges in format:")
print("Source Destination Weight\n")

# Input edges
for i in range(e):

    src = input("Enter source vertex: ")
    dest = input("Enter destination vertex: ")
    weight = int(input("Enter weight: "))

    # Undirected graph
    graph[src].append((dest, weight))
    graph[dest].append((src, weight))

    print()

# Dijkstra Algorithm
def dijkstra(start):

    # Store shortest distances
    distances = {}

    # Initially infinity
    for vertex in graph:
        distances[vertex] = float('inf')

    distances[start] = 0

    # Min Heap
    min_heap = [(0, start)]

    visited = set()

    while min_heap:

        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        # Check neighbors
        for neighbor, weight in graph[current_vertex]:

            distance = current_distance + weight

            # Update shorter distance
            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Input source vertex
start_vertex = input("\nEnter source vertex: ")

# Run algorithm
shortest_distances = dijkstra(start_vertex)

# Display output
print("\nShortest Distances from Source Vertex:\n")

for vertex, distance in shortest_distances.items():
    print(f"{start_vertex} --> {vertex} = {distance}")