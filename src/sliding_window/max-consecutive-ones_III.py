def longestOnes(nums, k):
    n = len(nums)
    max_ones = float('-inf')  # Initialize the maximum length found so far
    l = r = 0  # Initialize left and right pointers for the sliding window
    zeroes = 0  # Count of zeros in the current window

    while r < n:
        if nums[r] == 0:
            zeroes += 1  # Increment zero count if current element is 0

        # If the number of zeros exceeds k, shrink the window from the left
        if zeroes > k:
            if nums[l] == 0:
                zeroes -= 1  # Decrement zero count if leftmost element is 0
            l += 1  # Move left pointer to the right

        # If the number of zeros is within the allowed limit, update max_ones
        if zeroes <= k:
            length = r - l + 1  # Current window length
            max_ones = max(length, max_ones)  # Update maximum length if needed

        r += 1  # Move right pointer to the right

    return max_ones

# Example usage:
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
