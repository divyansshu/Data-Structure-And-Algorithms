def canPartition(nums):
    # Calculate the total sum of the array
    totalSum = sum(nums)
    # If the total sum is odd, it's not possible to partition into two equal subsets
    if totalSum % 2 != 0: return False
    # The target sum for each subset is half of the total sum
    target = totalSum // 2

    # Helper function to try all combinations recursively
    def backtrack(i, total):
        # If we've reached the target sum, partition is possible
        if total == target: return True
        # If we've exceeded the target or reached the end, partition is not possible
        if total > target or i >= len(nums): return False

        # Try including nums[i] in the current subset or skipping it
        return backtrack(i+1, total+nums[i]) or backtrack(i+1, total)

    # Start the recursion from index 0 and sum 0
    return backtrack(0, 0)

# Test cases
print(canPartition([1,5,11,5]))  # True
print(canPartition([1,2,3,5]))   # False