from collections import deque

# Create graph
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

print("\nEnter edges (Undirected Graph):\n")

# Input edges
for i in range(e):

    u = input("Enter first vertex: ")
    v = input("Enter second vertex: ")

    graph[u].append(v)
    graph[v].append(u)

    print()

# DFS Traversal
visited_dfs = set()

def dfs(node):

    if node not in visited_dfs:

        print(node, end=" ")

        visited_dfs.add(node)

        for neighbor in graph[node]:

            dfs(neighbor)

# BFS Traversal
def bfs(start):

    visited_bfs = set()

    queue = deque([start])

    visited_bfs.add(start)

    while queue:

        node = queue.popleft()

        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited_bfs:

                visited_bfs.add(neighbor)

                queue.append(neighbor)

# Start vertex
start = input("Enter starting vertex: ")

# DFS Output
print("\nDFS Traversal:")

dfs(start)

# BFS Output
print("\n\nBFS Traversal:")

bfs(start)