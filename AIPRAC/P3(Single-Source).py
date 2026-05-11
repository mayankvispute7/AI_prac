# Dijkstra's Algorithm for Single Source Shortest Path

INF = 9999999

# Number of vertices
n = int(input("Enter number of vertices: "))

graph = []

print("\nEnter adjacency matrix row by row:")

# Input adjacency matrix
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))

    if len(row) != n:
        print("Error: Enter exactly", n, "values.")
        exit()

    graph.append(row)

# Source vertex
source = int(input("\nEnter source vertex: "))

# Distance array
distance = [INF] * n
distance[source] = 0

# Visited array
visited = [False] * n

# Dijkstra Algorithm
for _ in range(n):

    min_distance = INF
    u = -1

    # Find minimum distance vertex
    for i in range(n):
        if not visited[i] and distance[i] < min_distance:
            min_distance = distance[i]
            u = i

    visited[u] = True

    # Update distances
    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:

            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:
                distance[v] = new_distance

# Print shortest distances
print("\nShortest distances from source vertex", source)

for i in range(n):
    print(f"Vertex {i} --> Distance = {distance[i]}")