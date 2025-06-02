def lower_bound(arr, target):
    # Initialize lowerBound to length of array (default if not found)
    lowerBound = len(arr)
    low = 0
    high = len(arr) - 1
        
    # Binary search for the first index where arr[index] >= target
    while low <= high:
        mid = (low + high) // 2
            
        if arr[mid] >= target:
            # Potential lower bound found, move left to find earlier occurrence
            lowerBound = mid
            high = mid - 1
        else:
            # Move right if current mid is less than target
            low = mid + 1
    return lowerBound
    
def upper_bound(arr, target):
    # Initialize upperBound to length of array (default if not found)
    upperBound = len(arr)
    low = 0
    high = len(arr) - 1
        
    # Binary search for the first index where arr[index] > target
    while low <= high:
        mid = (low + high) // 2
            
        if arr[mid] > target:
            # Potential upper bound found, move left to find earlier occurrence
            upperBound = mid
            high = mid - 1
        else:
            # Move right if current mid is less than or equal to target
            low = mid + 1
    return upperBound        
    
def countFreq(arr, target):
    # The number of occurrences is the difference between upper and lower bounds
    return upper_bound(arr, target) - lower_bound(arr, target)

# Test cases
print(countFreq([1, 1, 2, 2, 2, 2, 3], 2))   # Output: 4
print(countFreq([1, 1, 2, 2, 2, 2, 3], 4))   # Output: 0
print(countFreq([8, 9, 10, 12, 12, 12], target = 12)) # Output: 3