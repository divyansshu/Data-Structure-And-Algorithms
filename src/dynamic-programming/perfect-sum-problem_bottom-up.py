def perfectSum(arr, target):
    n = len(arr)
    dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
    
    def find_zeroes_in_array(arr):
        return len([x for x in arr if x == 0])
    
    for i in range(n+1):
        for j in range(target+1):
            if j == 0:
                dp[i][j] = 2**find_zeroes_in_array(arr[:i])
            elif i == 0:
                dp[i][j] = 0
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]

# print(perfectSum([5, 2, 3, 10, 6, 8], target = 10))
# print(perfectSum( [2, 5, 1, 4, 3], target = 10))
# print(perfectSum([5, 7, 8], target = 3))
# print(perfectSum([35, 2, 8, 22], target = 0))
print(perfectSum([28, 4, 3, 27, 0, 24, 26], 24))