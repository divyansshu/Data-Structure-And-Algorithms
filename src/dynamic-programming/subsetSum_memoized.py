def isSubsetSum (arr, sum):
    n = len(arr)
    dp = [[None for _ in range(sum+1)] for _ in range(n+1)]
    def backtrack(i, total):
        if total == sum:
            return True
        if total > sum or i >= len(arr):
            return False
        if dp[i][total] is not None:
            return dp[i][total]
        
        include = backtrack(i+1, total+arr[i])
        exclude = backtrack(i+1, total)
        
        dp[i][total] =  include or exclude
        return dp[i][total]
    
    return backtrack(0, 0)

print(isSubsetSum([3, 34, 4, 12, 5, 2], sum = 9))   # True: 4+5 or 3+4+2
print(isSubsetSum([3, 34, 4, 12, 5, 2], sum = 30))  # False: No subset sums to 30
print(isSubsetSum([1, 2, 3], sum = 6))              # True: 1+2+3