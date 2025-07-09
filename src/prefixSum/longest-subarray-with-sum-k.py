def longestSubarray(arr, k): 
    n = len(arr)
    prefixSum = 0
    mp = {}  # Dictionary to store the first occurrence of each prefix sum
    maxlen = 0
        
    for i in range(n):
        prefixSum += arr[i]  # Update the prefix sum up to index i

        # If prefix sum equals k, the subarray from 0 to i has sum k
        if prefixSum == k:
            maxlen = i + 1
            
        # If (prefixSum - k) is seen before, subarray (j+1 to i) sums to k
        if prefixSum - k in mp:
            j = mp[prefixSum - k]
            maxlen = max(maxlen, i - j)
            
        # Store the first occurrence of the prefix sum
        if prefixSum not in mp:
            mp[prefixSum] = i
    return maxlen

# Example usages
print(longestSubarray([10, 5, 2, 7, 1, -10], k = 15))
print(longestSubarray([-5, 8, -14, 2, 4, 12], k = -5))
print(longestSubarray([10, -10, 20, 30], k = 5))
