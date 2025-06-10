def rotateby90(mat): 
    # n is the last index of the matrix (assuming square matrix)
    n = len(mat) - 1
    L = 0  # Left boundary of current layer
    R = n  # Right boundary of current layer
    
    # Process layers from outermost to innermost
    while L < R:
        # For each element in the current layer
        for i in range(R-L):
            T, B = L, R  # Top and Bottom boundaries
            # Save the top-left value
            temp = mat[T][L+i]
            # Move right to top
            mat[T][L+i] = mat[T+i][R]
            # Move bottom to right
            mat[T+i][R] = mat[B][R-i]
            # Move left to bottom
            mat[B][R-i] = mat[B-i][L]
            # Assign saved top-left to left
            mat[B-i][L] = temp
        # Move to the next inner layer
        L += 1
        R -= 1        
            
mat = [[1, 2, 3, 4],[5, 6,7,8],[9,10,11,12], [13,14,15,16]]
print(mat)            
rotateby90(mat)
print(mat)