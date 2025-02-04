'''
time complexity: O(n)
space complexity: O(1)
'''

def canJump(nums):
    # Initialize the maximum reachable index to 0
    maxReach = 0
    
    # Iterate through each index in the list
    for i in range(len(nums)):
        # If the current index is greater than the maximum reachable index, return False
        if i > maxReach: return False
        
        # Update the maximum reachable index
        maxReach = max(maxReach, i + nums[i])
        
        # If the maximum reachable index is greater than or equal to the last index, return True
        if maxReach >= len(nums) - 1: return True
    
    # If the loop completes, return True
    return True 

# Test cases
print(canJump([2,3,1,1,4]))   # Expected output: True
print(canJump([3,2,1,0,4]))   # Expected output: False
print(canJump([2,0,0]))       # Expected output: True
print(canJump([0]))           # Expected output: True