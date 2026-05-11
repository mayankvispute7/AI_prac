# Minimum Spanning Tree using Prim's Algorithm

INF = 9999999

# Input number of vertices
n = int(input("Enter number of vertices: "))

graph = []

print("\nEnter adjacency matrix row by row:")

# Input adjacency matrix
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))

    # Check correct row size
    if len(row) != n:
        print("Error: Enter exactly", n, "values.")
        exit()

    graph.append(row)

selected = [False] * n

# Start from vertex 0
selected[0] = True

print("\nEdge : Weight")

# MST contains n-1 edges
for _ in range(n - 1):

    minimum = INF
    x = 0
    y = 0

    for i in range(n):

        if selected[i]:

            for j in range(n):

                if not selected[j] and graph[i][j] != 0:

                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {graph[x][y]}")

    selected[y] = True