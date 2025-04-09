def majorityElement_I(arr):
    # Get the length of the array
    n = len(arr)
    
    # Initialize candidate and count variables
    candidate, count = None, 0
    
    # First pass: Find a potential candidate for the majority element
    for num in arr:
        if num == candidate:
            # If the current number matches the candidate, increment the count
            count += 1
        elif count == 0:
            # If count is zero, set the current number as the new candidate
            candidate, count = num, 1
        else:
            # Otherwise, decrement the count
            count -= 1
    
    # Second pass: Verify if the candidate is actually the majority element
    if arr.count(candidate) > n // 2:
        return candidate  # Return the candidate if it appears more than n/2 times
    
    # If no majority element is found, return None
    return None

# Test cases
print(majorityElement_I([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(majorityElement_I([3, 3, 4, 2, 3, 3, 5]))  # Output: 3
print(majorityElement_I([1, 2, 3, 4]))          # Output: None