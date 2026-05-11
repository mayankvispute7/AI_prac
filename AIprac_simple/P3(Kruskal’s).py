edges = [
    (1, 'B', 'C'),
    (2, 'A', 'B'),
    (3, 'A', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D')
]

parent = {}

vertices = ['A', 'B', 'C', 'D']

for v in vertices:
    parent[v] = v

def find(node):

    if parent[node] == node:
        return node

    return find(parent[node])

def union(u, v):

    root_u = find(u)

    root_v = find(v)

    parent[root_v] = root_u

mst_cost = 0

print("Edges in MST:")

for weight, u, v in edges:

    if find(u) != find(v):

        union(u, v)

        print(u, "-", v, "=", weight)

        mst_cost += weight

print("Total Cost:", mst_cost)