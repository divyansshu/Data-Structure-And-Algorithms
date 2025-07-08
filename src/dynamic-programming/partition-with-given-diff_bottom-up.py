def countPartitions(arr, d):
    # n: number of elements in arr
    n = len(arr)
    # total_sum: sum of all elements plus the given difference
    total_sum = sum(arr) + d
    # If total_sum is odd or sum(arr) < d, partition is not possible
    if total_sum % 2 != 0 or sum(arr) < d:
        return 0

    # target: sum we need to find subsets for
    target = total_sum // 2
    # Initialize DP table with -1
    dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]

    # Helper to count zeroes in a subarray
    def count_zeroes(arr):
        return len([x for x in arr if x == 0])

    # Fill DP table
    for i in range(n+1):
        for j in range(target+1):
            if j == 0:
                # If sum is 0, number of ways is 2^(number of zeroes in arr[:i])
                dp[i][j] = 2**count_zeroes(arr[:i])
            elif i == 0:
                # If no elements, can't form positive sum
                dp[i][j] = 0
            elif arr[i-1] <= j:
                # Include or exclude current element
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                # Exclude current element
                dp[i][j] = dp[i-1][j]
    # Return number of ways to partition
    return dp[n][target]

# Example test cases
print(countPartitions([5, 2, 6, 4], d = 3))
print(countPartitions([1, 1, 1, 1], d = 0 ))
print(countPartitions([1, 2, 1, 0, 1, 3, 3], d = 11))
print(countPartitions([0, 1, 2, 2, 2, 3, 0, 3, 0, 1], 12))
print(countPartitions([0, 3, 0, 1, 2], 2))