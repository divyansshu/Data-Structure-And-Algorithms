'''
question link: https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1
'''

def minimumDifference(nums):
    n = len(nums)
    total = sum(nums)
    # dp[i][j] will be True if a subset of the first i elements has sum equal to j
    dp = [[None for _ in range(total+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(total+1):
            if j == 0:
                # Sum 0 is always possible (empty subset)
                dp[i][j] = True
            elif i == 0:
                # Non-zero sum is not possible with 0 elements
                dp[i][j] = False
            elif nums[i-1] <= j:
                # Include or exclude the current element
                dp[i][j] = dp[i-1][j - nums[i-1]] or dp[i-1][j]
            else:
                # Exclude the current element
                dp[i][j] = dp[i-1][j]
    
    # Find the largest j (<= total//2) such that dp[n][j] is True
    # This minimizes the difference between the two subset sums
    for i in range(total // 2, -1, -1):
        if dp[n][i]:
            return (total - 2 * i)

print(minimumDifference([1, 6, 11, 5]))
print(minimumDifference([1, 4]))
print(minimumDifference([1]))