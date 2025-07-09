'''
question link: https://leetcode.com/problems/target-sum/description/
''' 

def findTargetSumWays(arr, target):
    n = len(arr)
    # Calculate the transformed subset sum target
    total_sum = sum(arr) + target
    # If total_sum is odd or target is not achievable, return 0
    if total_sum % 2 != 0 or target > sum(arr) or total_sum < 0:
        return 0
    target2 = total_sum // 2
    # Initialize DP table with -1
    dp = [[-1 for _ in range(target2+1)]for _ in range(n+1)]
    
    def count_zeroes(arr):
        # Helper to count number of zeroes in the array
        return len([x for x in arr if x == 0])
    
    # Fill the DP table
    for i in range(n+1):
        for j in range(target2+1):
            if j == 0:
                # If sum is 0, number of ways is 2^(number of zeroes in arr[:i])
                dp[i][j] = 2**count_zeroes(arr[:i])
            elif i == 0:
                # No elements to form positive sum
                dp[i][j] = 0
            elif arr[i-1] <= j:
                # Include or exclude current element
                dp[i][j] = dp[i-1][j - arr[i-1]] + dp[i-1][j]
            else:
                # Exclude current element
                dp[i][j] = dp[i-1][j]
    return dp[n][target2]

# Example test cases
print(findTargetSumWays([1,1,1,1,1], target = 3))
print(findTargetSumWays([1], target = 1))
print(findTargetSumWays([100, 100], target = -400))  
print(findTargetSumWays([0], target = 0))  