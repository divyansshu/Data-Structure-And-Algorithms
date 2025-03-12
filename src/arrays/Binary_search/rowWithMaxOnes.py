class Solution:
    def rowWithMax1s(self, arr):
        # Get the number of rows and columns in the matrix
        rows, cols = len(arr), len(arr[0])
        rowWithMaxOnes = -1  # Initialize the row with the maximum number of 1s
        maxCount = 0  # Initialize the maximum count of 1s found

        # Helper function to find the index of the first 1 in a row using binary search
        def firstOneIndex(row):
            left, right = 0, cols - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if arr[row][mid] == 1: 
                    right = mid - 1  # Move left if a 1 is found
                else: 
                    left = mid + 1  # Move right if a 0 is found
            return left  # Return the index of the first 1 or the position where 1 should be
        
        # Iterate through each row to find the row with the maximum number of 1s
        for row in range(rows):
            firstOne = firstOneIndex(row)  # Get the index of the first 1 in the current row
            onesCount = cols - firstOne  # Calculate the number of 1s in the current row
            if onesCount > maxCount:  # Update if the current row has more 1s than the previous maximum
                maxCount = onesCount
                rowWithMaxOnes = row  # Update the row with the maximum number of 1s
        return rowWithMaxOnes  # Return the row index with the maximum number of 1s

# Example usage
arr = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

solution = Solution()
print(solution.rowWithMax1s(arr))  # Output the row index with the maximum number of 1s
