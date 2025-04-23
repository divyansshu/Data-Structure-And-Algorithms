def missingNumber(arr):
    # Convert the input array to a set to remove duplicates and allow O(1) lookups
    arr_set = set(arr)
    
    # Find the maximum value in the set
    Max = max(arr_set)
    
    # If the maximum value is less than 0, the smallest missing positive number is 1
    if Max < 0: 
        return 1
    
    # Iterate through numbers from 1 to Max
    for i in range(1, Max + 1):
        # If a number is not in the set, return it as the missing positive number
        if i not in arr_set:
            return i
    
    # If all numbers from 1 to Max are present, the missing number is Max + 1
    return Max + 1 

# Test cases
print(missingNumber([2, -3, 4, 1, 1, 7]))   # Expected output: 3
print(missingNumber([5, 3, 2, 5, 1]))       # Expected output: 4
print(missingNumber([-8, 0, -1, -4, -3]))   # Expected output: 1
print(missingNumber([1, 2, 3, 4, 5, 6]))    # Expected output: 7