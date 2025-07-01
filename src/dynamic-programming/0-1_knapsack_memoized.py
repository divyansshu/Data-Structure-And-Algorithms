def knapsack(W, val, wt):
    n = len(wt)
    # Initialize a 2D dp array with -1, dimensions (n+1) x (W+1)
    dp = [[-1 for _ in range(W+1)] for _ in range(n+1)]

    def backtrack(n, w):
        # Base case: no items left or capacity is 0
        if n == 0 or w == 0:
            return 0
        # If value already computed, return it (memoization)
        if dp[n][w] != -1:
            return dp[n][w]
        # If current item's weight is less than or equal to remaining capacity
        if wt[n-1] <= w:
            # Include the item or exclude it, take the maximum
            dp[n][w] = max(
                val[n-1] + backtrack(n-1, w - wt[n-1]),  # Include item
                backtrack(n-1, w)                        # Exclude item
            )
        else:
            # Cannot include the item, move to next
            dp[n][w] = backtrack(n-1, w)
        return dp[n][w]

    return backtrack(n, W)

# Test cases
print(knapsack(W=4, val=[1, 2, 3], wt=[4, 5, 1]))      # Output: 3
print(knapsack(W=3, val=[1, 2, 3], wt=[4, 5, 6]))      # Output: 0
print(knapsack(W=5, val=[10, 40, 30, 50], wt=[5, 4, 2, 3]))  # Output: 90