def combine(n, k):
    res = []  # This will store all the combinations

    def backtrack(idx, curr):
        # If the current combination is of length k, add a copy to results
        if len(curr) == k:
            res.append(curr[:])
            return

        # Try all possible next elements
        for i in range(idx, n+1):
            curr.append(i)           # Choose the next element
            backtrack(i+1, curr)     # Recurse with the next index
            curr.pop()               # Backtrack: remove the last element

    backtrack(1, [])  # Start from 1 with an empty combination
    return res

print(combine(4, 2))            