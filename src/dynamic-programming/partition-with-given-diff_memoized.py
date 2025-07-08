def countPartitions(arr, d):
    # n: number of elements in arr
    n = len(arr)
    # total_sum: sum of all elements plus the given difference
    total_sum = sum(arr) + d
    # If total_sum is odd or sum(arr) < d, partition is not possible
    if total_sum % 2 != 0 or sum(arr) < d:
        return 0

    # target: the sum each subset should reach for the required difference
    target = total_sum // 2
    # dp: memoization table, initialized to -1
    dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]

    def backtrack(i, total):
        # If current total exceeds target, no valid partition
        if total > target:
            return 0

        # If all elements are considered, check if total equals target
        if i == len(arr):
            return 1 if total == target else 0

        # Return cached result if already computed
        if dp[i][total] != -1:
            return dp[i][total]

        # Include arr[i] in the current subset or exclude it
        dp[i][total] = backtrack(i+1, total+arr[i]) + backtrack(i+1, total)
        return dp[i][total]

    # Start recursion from index 0 and total 0
    return backtrack(0, 0)

# Example usages
print(countPartitions([5, 2, 6, 4], d = 3))
print(countPartitions([1, 1, 1, 1], d = 0 ))
print(countPartitions([1, 2, 1, 0, 1, 3, 3], d = 11))
print(countPartitions([0, 1, 2, 2, 2, 3, 0, 3, 0, 1], 12))