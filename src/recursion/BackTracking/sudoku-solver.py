def solveSudoku(board):
    # Helper function to check if it's safe to place a digit at (row, col)
    def isSafe(row, col, digit):
        # Check the row for the same digit
        for c in range(9):
            if board[row][c] == digit:
                return False

        # Check the column for the same digit
        for r in range(9):
            if board[r][col] == digit:
                return False

        # Check the 3x3 subgrid for the same digit
        sr = (row // 3) * 3  # starting row of the 3x3 grid
        sc = (col // 3) * 3  # starting col of the 3x3 grid
        for i in range(sr, sr+3):
            for j in range(sc, sc+3):
                if board[i][j] == digit:
                    return False
        return True

    # Recursive helper function to solve the board
    def backtrack(row, col):
        # If we've reached the end of the board, solution is found
        if row == 9:
            return True

        # Move to the next cell
        nextrow, nextcol = row, col+1
        if nextcol == 9:
            nextrow += 1
            nextcol = 0

        # If the current cell is already filled, move to the next cell
        if board[row][col] != '.':
            return backtrack(nextrow, nextcol)

        # Try placing digits 1-9 in the current cell
        for digit in '123456789':
            if isSafe(row, col, digit):
                board[row][col] = digit  # Place the digit
                if backtrack(nextrow, nextcol):  # Recurse
                    return True
                board[row][col] = '.'  # Backtrack if needed
        return False

    backtrack(0, 0)  # Start solving from the top-left cell

# Example usage
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)
print(board)