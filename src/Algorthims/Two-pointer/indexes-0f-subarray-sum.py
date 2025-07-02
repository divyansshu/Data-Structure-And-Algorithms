def subarraySum(arr, target):
    n = len(arr)
    start, end = 0, 0  # Initialize pointers for the sliding window
    curr = 0           # Current sum of the window

    for i in range(n):
        curr += arr[i]  # Add current element to the window sum

        # If current sum is greater than or equal to target, try to shrink the window from the left
        if curr >= target:
            end = i  # Mark the end of the window

            # Shrink the window as long as the sum is greater than target
            while curr > target and start < end:
                curr -= arr[start]  # Remove element from the left
                start += 1          # Move start pointer to the right

            # If the current sum equals the target, return the 1-based indices
            if curr == target:
                return [start + 1, end + 1]

    # If no subarray found, return [-1]
    return [-1]

# Test cases
print(subarraySum([1, 2, 3, 7, 5], target=12))  # Output: [2, 4]
print(subarraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target=15))  # Output: [1, 5]
print(subarraySum([5, 3, 4], target=22))  # Output: [-1]