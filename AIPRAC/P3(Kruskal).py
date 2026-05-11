# Kruskal's Minimum Spanning Tree Algorithm

# Find parent function
def find(parent, node):

    if parent[node] == node:
        return node

    return find(parent, parent[node])

# Union function
def union(parent, u, v):

    root_u = find(parent, u)
    root_v = find(parent, v)

    parent[root_v] = root_u

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Input vertex names
vertices = []

print("\nEnter vertex names:")

for i in range(n):
    vertex = input(f"Vertex {i+1}: ")
    vertices.append(vertex)

# Input number of edges
e = int(input("\nEnter number of edges: "))

edges = []

print("\nEnter edges in format:")
print("Source Destination Weight\n")

# Input edges
for i in range(e):

    src = input("Enter source vertex: ")
    dest = input("Enter destination vertex: ")
    weight = int(input("Enter weight: "))

    edges.append((weight, src, dest))

    print()

# Sort edges according to weight
edges.sort()

# Create parent dictionary
parent = {}

for vertex in vertices:
    parent[vertex] = vertex

mst_cost = 0

print("\nEdges in Minimum Spanning Tree:\n")

# Kruskal Algorithm
for weight, u, v in edges:

    # Check cycle
    if find(parent, u) != find(parent, v):

        union(parent, u, v)

        print(f"{u} -- {v}  Weight = {weight}")

        mst_cost += weight

# Final output
print("\nMinimum Spanning Tree Cost =", mst_cost)