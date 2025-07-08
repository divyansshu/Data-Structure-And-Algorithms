def countPartitions(arr, d):
    # Calculate the total sum needed for one subset
    total_sum = sum(arr) + d

    # If total_sum is odd or sum(arr) < d, partition is not possible
    if total_sum % 2 != 0 or sum(arr) < d:
        return 0

    # The target sum for one subset
    target = total_sum // 2

    # Recursive helper function to count subsets with sum equal to target
    def backtrack(i, total):
        # If all elements are considered, check if current sum equals target
        if i == len(arr):
            return 1 if total == target else 0

        # Include current element in the subset or exclude it
        return backtrack(i+1, total+arr[i]) + backtrack(i+1, total)

    # Start recursion from index 0 and sum 0
    return backtrack(0, 0)

# Test cases
print(countPartitions([5, 2, 6, 4], d = 3))
print(countPartitions([1, 1, 1, 1], d = 0 ))
print(countPartitions([1, 2, 1, 0, 1, 3, 3], d = 11))
print(countPartitions([0, 1, 2, 2, 2, 3, 0, 3, 0, 1], 12))
