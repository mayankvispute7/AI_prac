# N-Queens Problem using Backtracking and Branch & Bound

# Function to check safe position
def is_safe(row, col, columns, left_diagonal, right_diagonal, n):

    # Check column
    if columns[col]:
        return False

    # Check left diagonal
    if left_diagonal[row - col + n - 1]:
        return False

    # Check right diagonal
    if right_diagonal[row + col]:
        return False

    return True


# Function to solve N-Queens
def solve_nqueens(row, board,
                  columns,
                  left_diagonal,
                  right_diagonal,
                  n):

    global solution_found

    # All queens placed
    if row == n:

        print(board)

        solution_found = True
        return

    # Try all columns
    for col in range(n):

        # Check safe position
        if is_safe(row, col,
                   columns,
                   left_diagonal,
                   right_diagonal, n):

            # Place queen
            board[row] = col

            columns[col] = 1
            left_diagonal[row - col + n - 1] = 1
            right_diagonal[row + col] = 1

            # Recursive call
            solve_nqueens(row + 1,
                          board,
                          columns,
                          left_diagonal,
                          right_diagonal,
                          n)

            # Backtrack
            columns[col] = 0
            left_diagonal[row - col + n - 1] = 0
            right_diagonal[row + col] = 0


# Main Program
n = int(input("Enter value of N: "))

board = [-1] * n

# Arrays for Branch and Bound
columns = [0] * n
left_diagonal = [0] * (2 * n - 1)
right_diagonal = [0] * (2 * n - 1)

solution_found = False

print("\nSolutions:\n")

# Solve problem
solve_nqueens(0,
              board,
              columns,
              left_diagonal,
              right_diagonal,
              n)

# If no solution
if not solution_found:
    print("No solution exists")