def isSafe(row, col, board, n):
    # Check if there is a queen in the same row
    for c in range(n):
        if board[row][c] == 'Q':
            return False

    # Check if there is a queen in the same column
    for r in range(n):
        if board[r][col] == 'Q':
            return False

    # Check upper left diagonal for a queen
    r = row
    c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1

    # Check upper right diagonal for a queen
    r = row
    c = col
    while r >= 0 and c < n:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c += 1

    # If no queens threaten the position, it's safe
    return True


def solveNQueens(n):
    res = []  # To store all possible solutions
    board = [['.'] * n for i in range(n)]  # Initialize the chessboard

    def backtrack(row):
        # If all rows are filled, add the current board configuration to results
        if row == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if isSafe(row, col, board, n):
                board[row][col] = 'Q'  # Place queen
                backtrack(row + 1)     # Move to next row
                board[row][col] = '.'  # Remove queen (backtrack)

    backtrack(0)  # Start from the first row
    return res

print(solveNQueens(4))