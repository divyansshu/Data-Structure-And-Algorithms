def combinationSum(arr, target):
    res = []  # This will store all valid combinations

    def backtrack(i, curr, total):
        # If index is out of bounds or total exceeds target, stop exploring this path
        if i >= len(arr) or total > target:
            return

        # If the current total equals the target, add a copy of current combination to result
        if total == target:
            res.append(curr[:])
            return

        # Include arr[i] in the current combination and recurse
        curr.append(arr[i])
        backtrack(i, curr, total + arr[i])
        curr.pop()  # Backtrack: remove last element

        # Exclude arr[i] and move to the next index
        backtrack(i+1, curr, total)

    backtrack(0, [], 0)  # Start backtracking from index 0, empty combination, and total 0
    return res

print(combinationSum([2,3,5], 8))
