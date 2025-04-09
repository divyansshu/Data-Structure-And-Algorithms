def majorityElement_II(arr):
    # Get the length of the array
    n = len(arr)
    
    # Initialize two potential candidates and their respective counts
    candidate1, count1 = None, 0
    candidate2, count2 = None, 0
    
    # First pass: Find potential candidates for majority elements
    for num in arr:
        if num == candidate1:  # If the current number matches candidate1, increment its count
            count1 += 1
        elif num == candidate2:  # If the current number matches candidate2, increment its count
            count2 += 1
        elif count1 == 0:  # If count1 is zero, assign the current number as candidate1
            candidate1, count1 = num, 1
        elif count2 == 0:  # If count2 is zero, assign the current number as candidate2
            candidate2, count2 = num, 1
        else:  # If the current number matches neither candidate and both counts are non-zero, decrement both counts
            count1 -= 1
            count2 -= 1           

    # Second pass: Verify the candidates by counting their occurrences
    result = []
    for candidate in [candidate1, candidate2]:
        # Check if the candidate appears more than n//3 times and is not already in the result
        if arr.count(candidate) > n // 3 and candidate not in result:
            result.append(candidate)
    
    return result  # Return the list of majority elements

# Test cases to verify the implementation
print(majorityElement_II([1, 2, 2, 3, 1, 1, 2, 2]))  # Output: [1, 2]
print(majorityElement_II([1, 2, 3, 4]))  # Output: []
print(majorityElement_II([3, 2, 3]))  # Output: [3]
print(majorityElement_II([1, 1, 1, 3, 3, 2, 2, 2]))  # Output: [1, 2]
print(majorityElement_II([1]))  # Output: [1]
print(majorityElement_II([7, 7, 7, 7, 7]))  # Output: [7]
print(majorityElement_II([1, 2, 3, 1, 2, 3, 1]))  # Output: [1]