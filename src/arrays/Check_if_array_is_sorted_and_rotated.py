def check(nums):
    n = len(nums)  # Get the length of the array
    count = 0  # Initialize a counter to count the number of rotations
    
    for i in range(n):
        # Check if the current element is greater than the next element
        # Use modulo to wrap around to the beginning of the array
        if nums[i] > nums[(i+1) % n]:
            count += 1  # Increment the counter if the condition is true
    
    # If the counter is less than or equal to 1, the array is sorted and rotated
    return count <= 1        

# Test cases
print(check([2,1,3,4]))  # False, not sorted and rotated
print(check([3,4,5,1,2]))  # True, sorted and rotated
print(check([1,2,3]))  # True, sorted but not rotated