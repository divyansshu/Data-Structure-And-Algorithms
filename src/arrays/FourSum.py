'''
time complexity: O(n^3)
Space complexity: O(1)
'''

def fourSum(nums, target):
    n = len(nums)
    # If there are less than 4 numbers, return an empty list
    if n < 4:
        return []
    
    # Sort the array to make it easier to avoid duplicates and use two pointers
    nums.sort()
    quadruplets = [] 
    
    # Iterate through the array with the first pointer
    for i in range(n-3):
        # Skip duplicate elements for the first pointer
        if i > 0 and nums[i] == nums[i-1]: continue
        
        # Iterate through the array with the second pointer
        for j in range(i+1, n-2):
            # Skip duplicate elements for the second pointer
            if j > i+1 and nums[j] == nums[j-1]: continue
            
            # Initialize two pointers for the remaining part of the array
            left , right = j+1, n-1
            
            # Use the two pointers to find the remaining two numbers
            while left < right:
                result = nums[i] + nums[left] + nums[right] + nums[j]
                if result == target:
                    # If the sum matches the target, add the quadruplet to the result list
                    quadruplets.append([nums[i], nums[left], nums[right], nums[j]])
                    
                    # Move the left pointer to the right and the right pointer to the left
                    left += 1
                    right -= 1
                    
                    # Skip duplicate elements for the left pointer
                    while left < right and nums[left] == nums[left - 1]: left += 1
                    # Skip duplicate elements for the right pointer
                    while left < right and nums[right] == nums[right+1]: right -= 1
                elif result < target:
                    # If the sum is less than the target, move the left pointer to the right
                    left += 1
                else:
                    # If the sum is greater than the target, move the right pointer to the left
                    right -= 1    
            
    # Print the list of quadruplets
    print(quadruplets)
    
# Test cases
fourSum([1,0,-1,0,-2,2], 0)                        
fourSum([2,2,2,2,2], 8)                        
fourSum([0,0,0,0], 0)                        