import heapq
from queue import PriorityQueue

# Function to find the kth smallest element using heapq
def kthSmallest(arr, k):
    # Convert the list into a min-heap
    heapq.heapify(arr)
    # Pop the smallest element k times
    for _ in range(k):
        kth_smallest = heapq.heappop(arr)
    # The kth popped element is the kth smallest
    return kth_smallest

# Function to find the kth smallest element using PriorityQueue
def kthSmallest_method2(arr, k):
    # Create a max-heap using PriorityQueue by inserting negative values
    pq = PriorityQueue()
   
    for num in arr:
        # Insert the negative of the number to simulate a max-heap
        pq.put((-num, num))
        # If the heap size exceeds k, remove the largest element
        if pq.qsize() > k:
            pq.get()
    
    # The root of the heap is the kth smallest element
    return pq.get()[1]

# Example usage
print(kthSmallest([7, 10, 4, 3, 20, 15], 3))
print(kthSmallest_method2([7, 10, 4, 3, 20, 15], 3))