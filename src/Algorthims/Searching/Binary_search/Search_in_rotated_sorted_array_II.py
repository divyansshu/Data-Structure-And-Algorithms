def search(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        
        if nums[mid] == target:
            return True  # Target found at mid
        
        # If duplicates are found at the boundaries, shrink the search space
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
            continue
        
        # determin which half is sorted
        if nums[left] <= nums[mid]:  # left half is sorted
            # Check if the target is in the left half
            if nums[left] <= target < nums[mid]: 
                right = mid - 1
            else: 
                left = mid + 1  # Search right half
                
        else:  # If the right half is sorted
            # Check if the target is in the right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1 # Search left half
                    
    return False  # Target not found

# Test cases
print(search([2,5,6,0,0,1,2], 0))  # True, target 0 is in the array
print(search([2,5,6,0,0,1,2], 3))  # False, target 3 is not in the array
print(search([3,4,4,6,2], 3))      # True, target 3 is in the array