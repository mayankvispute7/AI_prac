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

# Prim's Algorithm
def prim(start):

    visited = set()

    # Min heap stores (weight, node)
    min_heap = [(0, start)]

    total_cost = 0

    print("\nEdges in Minimum Spanning Tree:\n")

    while min_heap:

        cost, node = heapq.heappop(min_heap)

        if node not in visited:

            visited.add(node)
            total_cost += cost

            print(f"Visited Node: {node}  Cost: {cost}")

            # Check neighbors
            for neighbor, weight in graph[node]:

                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

    return total_cost

# Start vertex
start_vertex = input("\nEnter starting vertex: ")

# Run algorithm
minimum_cost = prim(start_vertex)

# Final output
print("\nMinimum Spanning Tree Cost =", minimum_cost)