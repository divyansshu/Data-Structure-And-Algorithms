def exist(board, word):
    # Get the number of rows and columns in the board
    rows, cols = len(board), len(board[0])
    path = set()  # To keep track of visited cells in the current path

    def backtrack(r, c, i):
        # If all characters are found, return True
        if i == len(word):
            return True
        # Check boundaries, character match, and if cell is already used in the current path
        if (r < 0 or c < 0 or r >= rows or c >= cols or 
            word[i] != board[r][c] or (r, c) in path):
            return False

        # Mark the cell as visited
        path.add((r, c))
        # Explore all four directions: down, up, right, left
        res = (backtrack(r+1, c, i+1) or 
               backtrack(r-1, c, i+1) or 
               backtrack(r, c+1, i+1) or 
               backtrack(r, c-1, i+1))
        # Unmark the cell (backtrack)
        path.remove((r, c))
        return res

    # Try to find the word starting from each cell
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False

# Example usage
print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))