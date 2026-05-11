INF = 9999999

graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 7],
    [6, 8, 7, 0]
]

n = 4

selected = [False] * n

selected[0] = True

print("Edge : Weight")

for i in range(n - 1):

    minimum = INF

    x = 0
    y = 0

    for i in range(n):

        if selected[i]:

            for j in range(n):

                if not selected[j] and graph[i][j]:

                    if minimum > graph[i][j]:

                        minimum = graph[i][j]

                        x = i
                        y = j

    print(x, "-", y, ":", graph[x][y])

    selected[y] = True