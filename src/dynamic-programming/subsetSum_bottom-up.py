def isSubsetSum(arr, sum):
    n = len(arr)
    # Create a 2D DP table where dp[i][j] will be True if a subset of arr[0..i-1] has sum j
    dp = [[None for _ in range(sum+1)] for _ in range(n+1)]
    for r in range(n+1):
        for c in range(sum+1):
            if c == 0:
                # Sum 0 can always be achieved with an empty subset
                dp[r][c] = True
            elif r == 0:
                # Non-zero sum cannot be achieved with 0 elements
                dp[r][c] = False
            elif arr[r-1] <= c:
                # Include the current element or exclude it
                dp[r][c] = dp[r-1][c-arr[r-1]] or dp[r-1][c]
            else:
                # Current element is greater than sum, cannot include it
                dp[r][c] = dp[r-1][c]
    # The answer is whether sum can be achieved with all n elements
    return dp[n][sum]

# Test cases
print(isSubsetSum([3, 34, 4, 12, 5, 2], sum=9))   # True: 4+5 or 3+4+2
print(isSubsetSum([3, 34, 4, 12, 5, 2], sum=30))  # False: No subset sums to 30
print(isSubsetSum([1, 2, 3], sum=6))              # True: 1+2+3