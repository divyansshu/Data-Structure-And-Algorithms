def searchRowMatrix(mat, x): 
    # Iterate through each row in the matrix
    for row in mat:
        low = 0
        high = len(row) - 1
        # Perform binary search on the current row
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == x:
                # Element found
                return True
            elif row[mid] > x:
                # Search in the left half
                high = mid - 1
            else:
                # Search in the right half
                low = mid + 1
        # If element not found in the current row, return False
        return False
    
# Test cases
print(searchRowMatrix([[3, 4, 9],[2, 5, 6],[9, 25, 27]], x = 9))      # True
print(searchRowMatrix([[19, 22, 27, 38, 55, 67]], x = 56))            # False
print(searchRowMatrix([[1, 2, 9],[65, 69, 75]], x = 91))              # False