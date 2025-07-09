'''
question link: https://leetcode.com/problems/target-sum/description/
''' 

def findTargetSumWays(arr, target):
    # Calculate the total sum needed for the subset sum transformation
    total_sum = sum(arr) + target

    # If total_sum is odd or target is not achievable, return 0
    if total_sum % 2 != 0 or target > sum(arr):
        return 0

    # The new target for subset sum
    target2 = total_sum // 2

    # Initialize memoization table with -1
    dp = [[-1 for _ in range(target2+1)] for _ in range(len(arr)+1)]

    def backtrack(i, total):
        # If current total exceeds target2, no valid subset
        if total > target2:
            return 0      

        # If all elements are considered, check if total matches target2
        if i == len(arr):
            return 1 if total == target2 else 0
        
        # Return cached result if already computed
        if dp[i][total] != -1:
            return dp[i][total]
        
        # Include arr[i] in the subset or exclude it, and sum the ways
        dp[i][total] = backtrack(i+1, total+arr[i]) + backtrack(i+1, total)
        return dp[i][total]
        
    # Start backtracking from index 0 and total 0
    return backtrack(0, 0)

# Example test cases
print(findTargetSumWays([1,1,1,1,1], target = 3))
print(findTargetSumWays([1], target = 1))
print(findTargetSumWays([100, 100], target = -400))