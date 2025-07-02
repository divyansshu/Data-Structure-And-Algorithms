def canPartition(arr):
    n = len(arr)
    totalSum = sum(arr)
    # If total sum is odd, can't partition into two equal subsets
    if totalSum % 2 != 0: 
        return False
    target = totalSum // 2
    # Initialize DP table: dp[i][j] is True if subset sum j is possible with first i elements
    dp = [[None for _ in range(target+1)] for _ in range(n+1)]
    for r in range(n+1):
        for c in range(target+1):
            if c == 0:
                # Sum 0 is always possible (empty subset)
                dp[r][c] = True
            elif r == 0:
                # Can't form positive sum with 0 elements
                dp[r][c] = False
            elif arr[r-1] <= c:
                # Include current element or exclude it
                dp[r][c] = dp[r-1][c-arr[r-1]] or dp[r-1][c]
            else:
                # Can't include current element, exclude it
                dp[r][c] = dp[r-1][c]
    # Final answer: can we form 'target' sum with all n elements?
    return dp[n][target]

print(canPartition([1,5,11,5]))  # True
print(canPartition([1,2,3,5]))   # False