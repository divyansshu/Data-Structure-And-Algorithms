import heapq

def nearlySorted(arr, k):
    # Create a min heap with the first k+1 elements
    min_heap = arr[:k+1]
    heapq.heapify(min_heap)
    
    j = 0
    # Process the remaining elements in the array
    for i in range(k+1, len(arr)):
        # Extract the minimum element from heap and put it in the correct position
        arr[j] = heapq.heappop(min_heap)
        # Add the next element from the array to the heap
        heapq.heappush(min_heap, arr[i])
        j += 1
    
    # Place remaining elements from the heap into the array
    while min_heap:
        arr[j] = heapq.heappop(min_heap)
        j += 1
    return arr

# Example usage
print(nearlySorted([6, 5, 3, 2, 8, 10, 9], k = 3))
print(nearlySorted([1, 4, 5, 2, 3, 6, 7, 8, 9, 10], k = 2))