class SpiralMatrix_II:
        
    @staticmethod
    def generateSpiralMatrix(n: int):
        # Initialize an n x n matrix filled with zeros
        spiral = [[0] * n for _ in range(n)]
        
        # Define the boundaries of the matrix
        left = top = 0
        right = bottom = n - 1
        val = 1  # Start filling the matrix with 1
        
        # Continue filling the matrix in a spiral order until all boundaries are crossed
        while left <= right:
            # Fill the top row from left to right
            for col in range(left, right + 1):
                spiral[top][col] = val
                val += 1
            
            top += 1  # Move the top boundary down
            
            # Fill the right column from top to bottom
            for row in range(top, bottom + 1):
                spiral[row][right] = val
                val += 1
            
            right -= 1  # Move the right boundary left
            
            # Fill the bottom row from right to left
            for col in range(right, left - 1, -1):
                spiral[bottom][col] = val
                val += 1
            
            bottom -= 1  # Move the bottom boundary up
            
            # Fill the left column from bottom to top
            for row in range(bottom, top - 1, -1):
                spiral[row][left] = val
                val += 1
            
            left += 1  # Move the left boundary right
        
        # Print the resulting spiral matrix
        print(spiral)            
                
print('spiral order matrix II')
SpiralMatrix_II.generateSpiralMatrix(3)
