'''
time complexity: O(n)
space complexity: O(1)
'''

def canJump(nums):
    n = len(nums)
    if n == 1: 
        return 0  # If there's only one element, no jumps are needed
    
    maxReach = 0  # The farthest index that can be reached
    currJumpRange = 0  # The range of the current jump
    jumps = 0  # Number of jumps made
    
    for i in range(len(nums)):
        maxReach = max(maxReach, i + nums[i])  # Update the farthest index that can be reached
        
        if i == currJumpRange:  # If we've reached the end of the current jump range
            jumps += 1  # Increment the number of jumps
            currJumpRange = maxReach  # Update the current jump range to the farthest index that can be reached
            
            if currJumpRange >= n - 1:  # If the current jump range reaches or exceeds the last index
                return jumps  # Return the number of jumps needed
    
    return jumps  # Return the number of jumps needed

# Test cases
print(canJump([2,3,1,1,4]))  # Output: 2
print(canJump([2,3,0,1,4]))  # Output: 2
print(canJump([2,1,1,1,4]))  # Output: 3
print(canJump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))  # Output: 2
