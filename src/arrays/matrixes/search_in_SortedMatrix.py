def searchMatrix(mat, x):
    # Get the number of rows and columns
    n = len(mat)
    m = len(mat[0])
    # Set the search range for binary search (flattened index)
    low = 0
    high = (n * m) - 1
        
    while low <= high:
        # Find the middle index in the flattened array
        mid = (low + high) // 2
        # Convert the flattened index back to 2D indices
        row = mid // m
        col = mid % m
        # Check if the middle element is the target
        if mat[row][col] == x:
            return True
        # If the middle element is greater, search the left half
        elif mat[row][col] > x:
            high = mid - 1
        # If the middle element is smaller, search the right half
        else:
            low = mid + 1
    # Target not found
    return False

# Test cases
print(searchMatrix([[1, 5, 9], [14, 20, 21], [30, 34, 43]], x = 14))
print(searchMatrix([[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]], x = 42))
print(searchMatrix([[87, 96, 99], [101, 103, 111]], x = 101))