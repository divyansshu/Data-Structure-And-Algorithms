def minCostClimbingStair(cost):
    # res is unused, can be removed
    memo = {}  # Dictionary to store results of subproblems (memoization)

    def minCost(i):
        # If we've already computed minCost for step i, return it
        if i in memo:
            return memo[i]
        # If we've gone past the last step, cost is 0 (base case)
        if i >= len(cost):
            return 0
        # Recursively compute the minimum cost from step i
        # You can climb either 1 or 2 steps, so take the minimum of both options
        memo[i] = cost[i] + min(minCost(i+1), minCost(i+2))
        return memo[i]

    # You can start from step 0 or step 1, so take the minimum of both
    return min(minCost(0), minCost(1))

# Example usage:
print(minCostClimbingStair([10, 15, 20]))  # Output: 15
print(minCostClimbingStair([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Output: 6