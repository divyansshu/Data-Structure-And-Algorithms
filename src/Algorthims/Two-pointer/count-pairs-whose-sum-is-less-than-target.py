def countPairs(arr, target):
    n = len(arr)
    cnt = 0
    arr.sort()  # Sort the array to use two-pointer technique
    i, j = 0, n - 1  # Initialize two pointers: i at start, j at end
    while i < j:
        # If sum of current pair is greater than or equal to target, move right pointer left
        if arr[i] + arr[j] >= target:
            j -= 1
        else:
            # If sum is less than target, all pairs between i and j are valid
            cnt += j - i
            i += 1  # Move left pointer right to check next pair
    return cnt

# Example usage and test cases
print(countPairs([7, 2, 5, 3], target=8))
print(countPairs([5, 2, 3, 2, 4, 1], target=5))
print(countPairs([2, 1, 8, 3, 4, 7, 6, 5], target=7))