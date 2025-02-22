def longestConsecutive(nums):
    # If the list is empty, return 0
    if len(nums) == 0:
        return 0
    
    # Remove duplicates and sort the numbers
    nums2 = sorted(set(nums))
    # Initialize count for current sequence and maxCount for the longest sequence found
    count = maxCount = 1
    
    # Iterate through the sorted list
    for i in range(len(nums2)-1):
        # Check if the current number is consecutive to the next number
        if nums2[i] == nums2[i+1] - 1:
            count += 1  # Increment the count for the current sequence
        else:
            # Update maxCount if the current sequence is longer
            maxCount = max(count, maxCount)
            # Reset count for the new sequence
            count = 1
                
    # Return the maximum of maxCount and count to account for the last sequence
    return max(maxCount, count) 
    
# Example usage
nums = [1,0,1,2]
print(longestConsecutive(nums))           