def isSubsetSum(arr, sum):
    # Helper function to use backtracking
    def backtrack(i, total):
        # If current total equals target sum, subset found
        if total == sum:
            return True
        # If total exceeds sum or no more elements, no valid subset
        if total > sum or i >= len(arr):
            return False
        # Try including arr[i] in the subset or skipping it
        return backtrack(i+1, total+arr[i]) or backtrack(i+1, total)
    # Start backtracking from index 0 and total 0
    return backtrack(0, 0)

# Test cases
print(isSubsetSum([3, 34, 4, 12, 5, 2], sum = 9))   # True: 4+5 or 3+4+2
print(isSubsetSum([3, 34, 4, 12, 5, 2], sum = 30))  # False: No subset sums to 30
print(isSubsetSum([1, 2, 3], sum = 6))              # True: 1+2+3