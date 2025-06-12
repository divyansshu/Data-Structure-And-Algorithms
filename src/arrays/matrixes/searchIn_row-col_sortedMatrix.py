def matSearch(mat, x):
    # Get the last row and last column indices
    row = len(mat) - 1
    col = len(mat[0]) - 1

    # Start from the top-right corner of the matrix
    i, j = 0, col

    # Loop until we go out of bounds
    while i <= row and j >= 0:
        # If the current element is the target, return True
        if x == mat[i][j]:
            return True
        # If the target is greater, move down to the next row
        elif x > mat[i][j]:
            i += 1
        # If the target is smaller, move left to the previous column
        else:
            j -= 1
    # If not found, return False
    return False

# Test cases
print(matSearch([[3, 30, 38],[20, 52, 54],[35, 60, 69]], x = 62))     # False
print(matSearch([[18, 21, 27],[38, 55, 67]], x = 55))                 # True
print(matSearch([[1, 2, 3],[4, 5, 6],[7, 8, 9]], x = 3))              # True