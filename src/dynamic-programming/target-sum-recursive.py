'''
question link: https://leetcode.com/problems/target-sum/description/
''' 

def findTargetSumWays(arr, target):
    # Calculate the sum of all elements plus the target
    total_sum = sum(arr) + target

    # If total_sum is odd or target is greater than the sum of arr, no solution exists
    if total_sum % 2 != 0 or target > sum(arr):
        return 0

    # The problem reduces to finding subsets with sum = target2
    target2 = total_sum // 2

    def backtrack(i, total):
        # Base case: if we've considered all elements
        if i == len(arr):
            # If the current sum equals target2, we've found a valid subset
            return 1 if total == target2 else 0
        # Explore two possibilities: include arr[i] or exclude it
        return backtrack(i+1, total+arr[i]) + backtrack(i+1, total)

    return backtrack(0, 0)

# Test cases
print(findTargetSumWays([1,1,1,1,1], target = 3))  # Output: 5
print(findTargetSumWays([1], target = 1))          # Output: 1
print(findTargetSumWays([100, 100], target = -400))# Output: 0
