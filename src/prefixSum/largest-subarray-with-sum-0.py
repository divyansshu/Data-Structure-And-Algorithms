def maxLength(arr):
    n = len(arr)
    maxlen = 0  # To store the maximum length found
    presum = 0  # To store the prefix sum
    mp = {}     # Dictionary to store first occurrence of each prefix sum

    for i in range(n):
        presum += arr[i]  # Update prefix sum

        # If prefix sum is zero, subarray from 0 to i has sum 0
        if presum == 0:
            maxlen = i + 1

        # If prefix sum has been seen before, subarray between previous index+1 and i has sum 0
        if presum in mp:
            j = mp[presum]
            maxlen = max(maxlen, i - j)
        else:
            # Store first occurrence of this prefix sum
            mp[presum] = i

    return maxlen

# Example usages
print(maxLength([15, -2, 2, -8, 1, 7, 10, 23]))
print(maxLength([2, 10, 4]))
print(maxLength([1, 0, -4, 3, 1, 0]))