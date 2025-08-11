import heapq

'''
direct method
'''
def kLargest(arr, k):
    # Convert the list into a heap in-place
    heapq.heapify(arr)
    # Return the k largest elements using heapq.nlargest
    return heapq.nlargest(k, arr)

'''
manual method
'''
def kLargest_(arr, k):
    # Create a min-heap with the first k elements
    minH = arr[:k]
    heapq.heapify(minH)
    # Iterate over the rest of the elements
    for x in arr[k:]:
        # If current element is larger than the smallest in heap
        if x > minH[0]:
            # Replace the smallest with the current element
            heapq.heapreplace(minH, x)
    # Return the k largest elements in descending order
    return sorted(minH, reverse=True)

# Test cases
print(kLargest([12, 5, 787, 1, 23], k = 2))           # [787, 23]
print(kLargest([1, 23, 12, 9, 30, 2, 50], k = 3))     # [50, 30, 23]
print(kLargest([12, 23], k = 1))                      # [23]

print(kLargest_([12, 5, 787, 1, 23], k = 2))          # [787, 23]
print(kLargest_([1, 23, 12, 9, 30, 2, 50], k = 3))    # [50, 30, 23]
print(kLargest_([12, 23], k = 1))                     # [23]