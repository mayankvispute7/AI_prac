INF = 9999999

graph = [
    [0, 2, 4, 0],
    [2, 0, 1, 7],
    [4, 1, 0, 3],
    [0, 7, 3, 0]
]

n = 4

source = 0

distance = [INF] * n

distance[source] = 0

visited = [False] * n

for i in range(n):

    min_distance = INF

    u = -1

    for j in range(n):

        if not visited[j] and distance[j] < min_distance:

            min_distance = distance[j]

            u = j

    visited[u] = True

    for v in range(n):

        if graph[u][v] != 0 and not visited[v]:

            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:

                distance[v] = new_distance

print("Shortest Distances:")

for i in range(n):

    print("Vertex", i, "=", distance[i])