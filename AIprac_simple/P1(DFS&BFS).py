from collections import deque

# Undirected Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS
visited = set()

def dfs(node):

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor)

# BFS
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

# Run
print("DFS Traversal:")
dfs('A')

print("\nBFS Traversal:")
bfs('A')