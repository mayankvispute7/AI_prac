import heapq

# Heuristic Function (Manhattan Distance)
def heuristic(a, b):

    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# A* Algorithm
def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    open_list = []

    heapq.heappush(open_list, (0, start))

    came_from = {}

    g_cost = {}
    g_cost[start] = 0

    while open_list:

        _, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:

            path = []

            while current in came_from:

                path.append(current)

                current = came_from[current]

            path.append(start)

            path.reverse()

            return path

        x, y = current

        # Possible movements
        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        for nx, ny in neighbors:

            # Valid position check
            if 0 <= nx < rows and 0 <= ny < cols:

                # Check obstacle
                if grid[nx][ny] == 0:

                    new_cost = g_cost[current] + 1

                    if ((nx, ny) not in g_cost or
                        new_cost < g_cost[(nx, ny)]):

                        g_cost[(nx, ny)] = new_cost

                        f_cost = new_cost + heuristic((nx, ny), goal)

                        heapq.heappush(open_list,
                                       (f_cost, (nx, ny)))

                        came_from[(nx, ny)] = current

    return None


# Main Program
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("\nEnter grid values:")
print("0 = Free Path")
print("1 = Obstacle\n")

# Input grid
for i in range(rows):

    row = list(map(int, input(f"Row {i+1}: ").split()))

    grid.append(row)

# Start point
sx = int(input("\nEnter start row: "))
sy = int(input("Enter start column: "))

# Goal point
gx = int(input("\nEnter goal row: "))
gy = int(input("Enter goal column: "))

start = (sx, sy)
goal = (gx, gy)

# Run A*
path = astar(grid, start, goal)

# Output
if path:

    print("\nShortest Path Found:\n")
    print(path)

else:

    print("\nNo path found.")