def knapsack(W, val, wt):
    n = len(wt)
    # Helper function to solve knapsack using recursion
    def backtrack(n, w):
        # Base case: no items left or capacity is 0
        if n == 0 or w == 0:
            return 0
        # If weight of the nth item is less than or equal to current capacity
        if wt[n-1] <= w:
            # Return the maximum of two cases:
            # (1) nth item included
            # (2) nth item not included
            return max(
                val[n-1] + backtrack(n-1, w - wt[n-1]),  # Include item
                backtrack(n-1, w)                        # Exclude item
            )
        else:
            # If weight of nth item is more than capacity, skip it
            return backtrack(n-1, w)
    # Start recursion with all items and full capacity
    return backtrack(n, W)

# Test cases
print(knapsack(W=4, val=[1, 2, 3], wt=[4, 5, 1]))      # Output: 3
print(knapsack(W=3, val=[1, 2, 3], wt=[4, 5, 6]))      # Output: 0
print(knapsack(W=5, val=[10, 40, 30, 50], wt=[5, 4, 2, 3]))  # Output: 90