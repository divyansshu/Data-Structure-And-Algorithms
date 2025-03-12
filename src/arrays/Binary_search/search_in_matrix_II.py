def searchMatrix(matrix, target):
    # Start from the top-right corner of the matrix
    row = 0
    col = len(matrix[0]) - 1
    
    # Loop until we either find the target or exhaust the matrix bounds
    while col >= 0 and row < len(matrix):
        if target < matrix[row][col]:
            # If the target is less than the current element, move left
            col -= 1
        elif target > matrix[row][col]:
            # If the target is greater than the current element, move down
            row += 1
        else: 
            # If the target is equal to the current element, return True
            return True
    # If we exit the loop without finding the target, return False
    return False

# Test cases
print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target= 20))            
print(searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target= 5)) 