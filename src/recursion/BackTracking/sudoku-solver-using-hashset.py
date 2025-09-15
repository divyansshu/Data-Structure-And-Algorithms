def sudokuSolver(board):
    # Initialize sets to keep track of used digits in each row, column, and 3x3 box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    # Fill the sets with the initial digits from the board
    for r in range(9):
        for c in range(9):
            digit = board[r][c]
            if digit != '.':
                box_id = (r // 3) * 3 + (c // 3)  # Calculate box index
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box_id].add(digit)
    
    def backtrack(r, c):
        # If we've reached row 9, the board is solved
        if r == 9:
            return True
        # Move to the next cell
        nextrow, nextcol = r, c+1
        if nextcol == 9:
            nextrow += 1
            nextcol = 0

        # Skip filled cells
        if board[r][c] != '.':
            return backtrack(nextrow, nextcol)
                
        for digit in '123456789':
            box_id = (r // 3) * 3 + (c // 3)
            # Check if digit is already used in row, column, or box
            if digit in rows[r] or digit in cols[c] or digit in boxes[box_id]:
                continue
                    
            # Place digit and update sets
            board[r][c] = digit
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box_id].add(digit)
               
            # Recursively try to fill the rest of the board
            if backtrack(nextrow, nextcol):
                return True
            # Backtrack if not solvable
            board[r][c] = '.'
            rows[r].remove(digit)
            cols[c].remove(digit)
            boxes[box_id].remove(digit)   
        return False
                    
    # Start backtracking from the top-left cell
    backtrack(0,0)

# Example board
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
sudokuSolver(board)
print(board)