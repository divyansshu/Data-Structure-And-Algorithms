# time complexity: O(mlogn)
def searchMatrix(matrix, target):
    # Iterate through each row in the matrix
    for row in matrix:
        left, right = 0, len(row) - 1

        # If the target is greater than the last element of the row, skip this row
        if target > row[right]: continue
        # If the target is less than the first element of the row, stop searching
        if target < row[left]: break

        # Perform binary search within the row
        while left <= right:
            mid = (left + right) // 2

            # If the target is found, return True
            if target == row[mid]: return True
            # If the target is greater than the middle element, search the right half
            elif row[mid] < target:
                left = mid + 1
            # If the target is less than the middle element, search the left half
            else:
                right = mid - 1
    # If the target is not found in any row, return False
    return False 

# time complexity: O(logm) + O(logn)
def searchMatrix_method2(matrix, target):
    # Get the number of rows and columns in the matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # Initialize pointers for the top and bottom rows
    top, bott = 0, rows - 1
    
    # Perform binary search to find the correct row
    while top <= bott:
        row = (top + bott) // 2
        # If the target is greater than the last element of the current row, search in the lower rows
        if target > matrix[row][-1]:
            top = row + 1
        # If the target is less than the first element of the current row, search in the upper rows
        elif target < matrix[row][0]:
            bott = row - 1
        # If the target is within the range of the current row, break the loop
        else:
            break
    
    # If the target is not within any row range, return False
    if not top <= bott:
        return False
    
    # Perform binary search within the identified row
    row = (top + bott) // 2
    left, right = 0, cols - 1
    while left <= right:
        mid = (left + right) // 2
        # If the target is less than the middle element, search the left half
        if target < matrix[row][mid]:
            right = mid - 1
        # If the target is greater than the middle element, search the right half
        elif target > matrix[row][mid]:
            left = mid + 1
        # If the target is found, return True
        else:
            return True
    
    # If the target is not found in the row, return False
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]  
print(searchMatrix(matrix, target=3))  # Output: True
print(searchMatrix(matrix, target=13)) # Output: False

print(searchMatrix_method2(matrix, target=3))  # Output: True
print(searchMatrix_method2(matrix, target=13)) # Output: False
