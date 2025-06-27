def isValidSudoku(board):
    # Create a list of sets to track seen digits in each row, column, and 3x3 box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Iterate over each cell in the 9x9 board
    for r in range(9):
        for c in range(9):
            # Calculate the index for the corresponding 3x3 box
            box_id = ((r // 3) * 3) + c // 3
            digit = board[r][c]
            if digit != '.':  # Ignore empty cells
                # Check if the digit is already seen in the current row, column, or box
                if digit in rows[r] or digit in cols[c] or digit in boxes[box_id]:
                    return False  # Duplicate found, not a valid Sudoku
                # Add the digit to the respective row, column, and box sets
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box_id].add(digit)
    return True  # No duplicates found, valid Sudoku

# Test cases
print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))