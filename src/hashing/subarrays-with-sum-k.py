def countSubarrays(arr, k):
    cnt = 0  # Initialize count of subarrays
    currSum = 0  # Initialize current prefix sum
    prefixSum = {}  # Dictionary to store frequency of prefix sums

    for num in arr:
        currSum += num  # Update current prefix sum

        # If current prefix sum equals k, increment count
        if currSum == k:
            cnt += 1

        # If (currSum - k) exists in prefixSum, add its frequency to count
        if currSum - k in prefixSum:
            cnt += prefixSum[currSum - k]
        
        # Update the frequency of current prefix sum in the dictionary
        prefixSum[currSum] = prefixSum.get(currSum, 0) + 1

    return cnt

# Test cases
print(countSubarrays([10, 2, -2, -20, 10], k = -10))
print(countSubarrays([1, 2, 3], k = 3))
