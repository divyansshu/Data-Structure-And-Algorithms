def perfectSum(arr, target):
    n = len(arr)
    dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]
    def backtrack(i, total):
        if i == n:
            return 1 if total == target else 0
		
        if total > target:
            return 0
        
        if dp[i][total] != -1:
            return dp[i][total]
        
        cnt1 = backtrack(i+1, total+arr[i])
        cnt2 = backtrack(i+1, total)
        dp[i][total] = cnt1 + cnt2
        return dp[i][total]
		   
    return backtrack(0,0)

print(perfectSum([5, 2, 3, 10, 6, 8], target = 10))
print(perfectSum( [2, 5, 1, 4, 3], target = 10))
print(perfectSum([5, 7, 8], target = 3))
print(perfectSum([35, 2, 8, 22], target = 0))