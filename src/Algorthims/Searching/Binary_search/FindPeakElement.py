def findPeakElement(nums: list[int]) -> int:
    # Get the length of the input list
    n = len(nums)
    
    # Check if the list has only one element or if the first element is a peak
    if n == 1 or nums[0] > nums[1]: return 0
    # Check if the last element is a peak
    if nums[n-1] > nums[n-2]: return n-1
    
    # Initialize the left and right pointers for binary search
    left = 0
    right = n - 1
    
    # Perform binary search
    while left <= right:
        # Calculate the mid index
        mid = (left + right) // 2
        
        # Check if the mid element is a peak
        if (mid == 0 or nums[mid] > nums[mid-1]) and (mid == n-1 or nums[mid] > nums[mid+1]):
            return mid
        # If the left neighbor is greater, move the right pointer
        elif mid > 0 and nums[mid-1] > nums[mid]:
            right = mid - 1
        # Otherwise, move the left pointer
        else:
            left = mid + 1
    
    # Return -1 if no peak is found (though this should not happen with the given constraints)
    return -1        

# Test the function with a sample input
print(findPeakElement([1,2,1,3,5,6,4]))           
