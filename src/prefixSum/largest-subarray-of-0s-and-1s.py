def maxLen(arr):
    n = len(arr)
    maxlen = 0  # To store the maximum length found
    presum = 0  # To store the prefix sum (difference between count of 1s and 0s)
    mp = {}     # Dictionary to store the first occurrence index of each prefix sum

    for i in range(n):
        # Treat 0 as -1 and 1 as 1, so we can use prefix sum to find subarrays with equal 0s and 1s
        presum += -1 if arr[i] == 0 else 1

        # If prefix sum is 0, it means from index 0 to i, number of 0s and 1s are equal
        if presum == 0:
            maxlen = i + 1

        # If this prefix sum has been seen before, there is a subarray with equal 0s and 1s
        if presum in mp:
            j = mp[presum]
            maxlen = max(maxlen, i - j)
        else:
            # Store the first occurrence of this prefix sum
            mp[presum] = i

    return maxlen

# Test cases
print(maxLen([1, 0, 1, 1, 1, 0, 0]))
print(maxLen([0, 0, 1, 1, 0]))
print(maxLen([0]))
print(maxLen([0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]))