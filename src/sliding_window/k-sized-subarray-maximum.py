from collections import deque

def maxOfSubarrays(arr, k):
    st = deque()  # Deque to store useful elements for current window
    i = j = 0     # Window start (i) and end (j) pointers
    n = len(arr)
    res = []      # Result list to store maximums of each window
    while j < n:
        # Remove all elements smaller than current from the front
        while st and arr[j] > st[0]:
            st.popleft()
        st.append(arr[j])  # Add current element to the deque

        # If window size is reached
        if j - i + 1 == k:
            res.append(st[0])  # The front of deque is the max in current window
            # If the element going out is at the front, remove it
            if st[0] == arr[i]:
                st.popleft()
            i += 1  # Slide the window forward
        j += 1
    return res

# Example usage
print(maxOfSubarrays([1, 2, 3, 1, 4], k = 3))
print(maxOfSubarrays([8, 5, 10, 7, 9, 4, 15, 12], k = 4))
print(maxOfSubarrays([5, 1, 3, 4, 2], k = 1))