def canPartition(nums):
    n = len(nums)
    totalSum = sum(nums)
    # If total sum is odd, it's not possible to partition into two equal subsets
    if totalSum % 2 != 0: return False
    target = totalSum // 2
    # Initialize memoization table with None
    dp = [[None for _ in range(target+1)] for _ in range(n+1)]
    
    def backtrack(i, total):
        # If we've reached the target sum, partition is possible
        if total == target: return True
        # If sum exceeds target or we've used all numbers, not possible
        if total > target or i >= len(nums): return False
        
        # Return cached result if already computed
        if dp[i][total] is not None: return dp[i][total]
        
        # Choose to include nums[i] in the subset
        include = backtrack(i+1, total+nums[i])
        # Or choose to exclude nums[i] from the subset
        exclude = backtrack(i+1, total)
        # Store result in memoization table
        dp[i][total] = include or exclude
        return dp[i][total]
    
    return backtrack(0, 0)

print(canPartition([1,5,11,5]))  # True
print(canPartition([1,2,3,5]))   # False
