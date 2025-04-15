def getMinDiff(arr, k):
    # Get the number of elements in the array
    n = len(arr)
    
    # Sort the array to handle elements in order
    arr.sort()
    
    # Initialize the minimum difference as the difference between the largest and smallest elements
    min_diff = arr[-1] - arr[0]
    
    # Iterate through the array to calculate the minimum difference
    for i in range(n - 1):
        # Calculate the minimum height after adding/subtracting k
        min_height = min(arr[0] + k, arr[i + 1] - k)
        
        # Calculate the maximum height after adding/subtracting k
        max_height = max(arr[n - 1] - k, arr[i] + k)
        
        # If the minimum height becomes negative, skip this iteration
        if min_height < 0:
            continue
        
        # Calculate the difference between the maximum and minimum heights
        diff = max_height - min_height
        
        # Update the minimum difference if the current difference is smaller
        min_diff = min(min_diff, diff)
    
    # Return the minimum difference
    return min_diff

# Test cases
print(getMinDiff([1, 5, 8, 10], 2))  # Output: 5
print(getMinDiff([3, 9, 12, 16, 20], 3))  # Output: 11