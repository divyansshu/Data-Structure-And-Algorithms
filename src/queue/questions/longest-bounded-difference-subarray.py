'''
Brute-force approach:
time complexity: O(n^3)
space complexity: O(1)
Finds the longest subarray where the difference between max and min is <= limit.
'''
def longest_subarray(arr, limit):
    n = len(arr)
    maxlen = 1      # Store the length of the longest valid subarray found
    begin = 0       # Store the starting index of the longest valid subarray
    for i in range(n):              # Try every possible starting index
        for j in range(i, n):       # Try every possible ending index
            mini = float('inf')     # Initialize minimum value in subarray
            maxi = float('-inf')    # Initialize maximum value in subarray
            
            # Find min and max in current subarray arr[i:j+1]
            for k in range(i, j+1):
                mini = min(mini, arr[k])
                maxi = max(maxi, arr[k])
                
            # Check if difference is within limit and update result if longer subarray found
            if maxi - mini <= limit and maxlen < j - i + 1:
                maxlen = j - i + 1
                begin = i
    # Return the longest valid subarray
    return arr[begin: begin + maxlen]
                    
                    
from collections import deque

'''
Optimized approach using monotonic queues:
time complexity: O(n)
space complexity: O(n)
Finds the longest subarray where the difference between max and min is <= limit.
'''
def longestSubarray(arr, limit):
    n = len(arr)
    minqueue = deque()   # Monotonic increasing queue for minimum values
    maxqueue = deque()   # Monotonic decreasing queue for maximum values
     
    start = end = 0      # Window pointers
    resstart = resend = 0 # Store the start and end of the longest valid subarray
      
    while end < n:
        # Maintain minqueue: remove elements larger than arr[end]
        while minqueue and arr[minqueue[-1]] > arr[end]:
            minqueue.pop()
            
        # Maintain maxqueue: remove elements smaller than arr[end]
        while maxqueue and arr[maxqueue[-1]] < arr[end]:
            maxqueue.pop()
            
        # Add current index to both queues
        minqueue.append(end)
        maxqueue.append(end)
            
        # Shrink window from left if difference exceeds limit
        while arr[maxqueue[0]] - arr[minqueue[0]] > limit:
            if start == minqueue[0]:
                minqueue.popleft()
            if start == maxqueue[0]:
                maxqueue.popleft()
            start += 1
            
        # Update result if current window is longer
        if end - start > resend - resstart:
            resend, resstart = end, start
            
        end += 1
        
    # Return the longest valid subarray
    return arr[resstart: resend+1]

# Example usage and test cases
print(longest_subarray([8, 4, 2, 6, 7],4))
print(longest_subarray([15, 10, 1, 2, 4, 7, 2], 5 ))

print(longestSubarray([8, 4, 2, 6, 7],4))
print(longestSubarray([15, 10, 1, 2, 4, 7, 2], 5 ))