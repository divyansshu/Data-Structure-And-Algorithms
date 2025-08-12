import heapq

def findClosestElements(arr, k, x):
    # Build a min-heap where each element is a tuple: (distance from x, value)
    min_heap = [(abs(num - x), num) for num in arr]
    heapq.heapify(min_heap)
    
    res = []
    # Extract the k elements with the smallest distance from x
    for _ in range(k):
        _, val = heapq.heappop(min_heap)
        res.append(val)
    # Return the result sorted in ascending order
    return sorted(res)
    
    
print(findClosestElements([1,2,3,4,5], k = 4, x = 3))
print(findClosestElements([1,1,2,3,4,5], k = 4, x = -1))