def longestOnes(nums, k):
    n = len(nums)
    max_ones = float('-inf')  # Initialize the maximum length found so far
    l = r = 0  # Left and right pointers for the sliding window
    zeroes = 0  # Count of zeroes in the current window

    while r < n:
        if nums[r] == 0:
            zeroes += 1  # Increment zero count if current element is 0

        # If zeroes in window exceed k, move left pointer to reduce zeroes
        while zeroes > k:
            if nums[l] == 0:
                zeroes -= 1  # Decrement zero count as we move past a zero
            l += 1  # Shrink window from the left

        # Update max_ones if current window is valid (zeroes <= k)
        if zeroes <= k:
            length = r - l + 1  # Current window length
            max_ones = max(length, max_ones)  # Update maximum length if needed

        r += 1  # Expand window to the right

    return max_ones

# Example usage:
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))
print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
