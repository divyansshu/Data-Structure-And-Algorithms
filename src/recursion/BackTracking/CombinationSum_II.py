def combinationSum(arr, target):
    arr.sort()  # Sort the array to handle duplicates easily
    res = []    # This will store the final list of combinations

    def backtrack(i, curr, total):
        # If the current total equals the target, add a copy of curr to results
        if total == target:
            res.append(curr[:])
            return
        
        # If index is out of bounds or total exceeds target, stop exploring this path
        if i >= len(arr) or total > target:
            return

        # Include arr[i] in the current combination
        curr.append(arr[i])
        backtrack(i+1, curr, total + arr[i])
        curr.pop()  # Backtrack: remove the last element added

        # Skip duplicates to avoid duplicate combinations
        while i+1 < len(arr) and arr[i] == arr[i+1]:
            i += 1
        # Exclude arr[i] and move to the next element
        backtrack(i+1, curr, total)

    backtrack(0, [], 0)  # Start backtracking from index 0, empty combination, and total 0
    return res

# Example usage
print(combinationSum([10,1,2,7,6,1,5], 8))
print(combinationSum([2,5,2,1,2], 5))
