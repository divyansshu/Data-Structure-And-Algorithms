def printSubArrays(arr):
    # Get the length of the array
    n = len(arr)
    
    # Loop over each element in the array as the starting point of the subarray
    for i in range(n):
        # Loop over each element from the current starting point to the end of the array
        for k in range(i, n):
            # Print the subarray from the current starting point to the current end point
            print(arr[i:k+1])

# Example array
arr = [3, 1, 2, 4]
# Call the function to print all subarrays of the given array
printSubArrays(arr)