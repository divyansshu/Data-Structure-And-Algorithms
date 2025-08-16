def canAttend(arr):
    # Sort the intervals by their start times
    arr.sort(key=lambda x: x[0])
    
    # Iterate through the sorted intervals and check for overlaps
    for i in range(1, len(arr)):
        # If the current meeting starts before the previous one ends, return False
        if arr[i][0] < arr[i-1][1]:
            return False
    # If no overlaps are found, return True
    return True

# Test cases
print(canAttend([[1, 4], [10, 15], [7, 10]]))  # Should return True
print(canAttend([[2, 4], [9, 12], [6, 10]]))   # Should return True