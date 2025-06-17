def combinationSum3(k , n):
    res = []    # List to store all valid combinations
    curr = []   # Current combination being built

    def backtrack(idx , total):
        # If the current combination has k numbers and sums to n, add to result
        if total == n and len(curr) == k:
            res.append(curr[:])
            return
        # If the sum exceeds n or combination size exceeds k, stop exploring
        if total > n or len(curr) >= k:
            return

        # Try all numbers from idx to 9
        for i in range(idx, 10):
            # If adding i exceeds n, no need to continue (since numbers are increasing)
            if total + i > n: break
            curr.append(i)                # Choose the number i
            backtrack(i+1, total+i)       # Recurse with next number and updated sum
            curr.pop()                    # Backtrack: remove last number

    backtrack(1, 0)   # Start with 1 and sum 0
    return res

print(combinationSum3(3,7))