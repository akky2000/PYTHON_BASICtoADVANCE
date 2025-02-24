def is_safe(board, row, col, n):
    # Check the same row on the left
    for i in range(col):
        if board[row][i] == 'Q':
            return False
        
    for j in range(row):
        if board[j][col] == 'Q':
            return False

    # Check the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the lower diagonal on the left
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, col, n):
    if col >= n:  # All queens are placed
        return True

    for i in range(n):
        if is_safe(board, i, col, n):  # Check if placing the queen is safe
            board[i][col] = 'Q'  # Place queen
            if solve_n_queens(board, col + 1, n):  # Recur to place the next queen
                return True
            board[i][col] = 0  # Backtrack

    return False

# Initialize the board and solve
n = 4
board = [[0] * n for _ in range(n)]
if solve_n_queens(board, 0, n):
    for row in board:
        print(row)
else:
    print("No solution exists")
