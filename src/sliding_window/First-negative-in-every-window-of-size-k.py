from collections import deque

def firstNegInt(arr, k):
    n = len(arr)
    i = j = 0  # Initialize window pointers
    res = []   # Result list to store first negative numbers
    queue = deque()  # Deque to store negative numbers in current window

    while j < n:
        # If current element is negative, add it to the queue
        if arr[j] < 0:
            queue.append(arr[j])

        # Check if window size has reached k
        if j - i + 1 == k:
            # If queue is empty, no negative number in window
            if len(queue) == 0:
                res.append(0)
            else:
                # The first negative number is at the front of the queue
                res.append(queue[0])
                # If the element going out of the window is the first negative, remove it from queue
                if queue[0] == arr[i]:
                    queue.popleft()
            # Slide the window forward
            i += 1
        # Expand the window
        j += 1
    return res

# Test cases
print(firstNegInt([-8, 2, 3, -6, 10], k=2))
print(firstNegInt([12, -1, -7, 8, -15, 30, 16, 28], k=3))
print(firstNegInt([12, 1, 3, 5], k=3))