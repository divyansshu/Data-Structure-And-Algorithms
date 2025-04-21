def maxSubarraySumCircular(nums):
    # Initialize variables to track the current max/min subarray sums
    # and the global max/min subarray sums
    curMax, curMin = 0, 0
    globMax, globMin = nums[0], nums[0]
    total = 0  # To store the total sum of the array

    for num in nums:
        # Update the current maximum subarray sum ending at the current element
        curMax = max(curMax + num, num)
        # Update the current minimum subarray sum ending at the current element
        curMin = min(curMin + num, num)
        # Add the current element to the total sum
        total += num

        # Update the global maximum subarray sum
        globMax = max(curMax, globMax)
        # Update the global minimum subarray sum
        globMin = min(curMin, globMin)

    # If the global maximum is positive, return the maximum of:
    # 1. The global maximum subarray sum (non-circular case)
    # 2. The total sum minus the global minimum subarray sum (circular case)
    # If the global maximum is negative, return it (all elements are negative)
    return max(globMax, (total - globMin)) if globMax > 0 else globMax

# Test cases
print(maxSubarraySumCircular([1, -2, 3, -2]))  # Output: 3
print(maxSubarraySumCircular([5, -3, 5]))      # Output: 10
print(maxSubarraySumCircular([-3, -2, -3]))    # Output: -2