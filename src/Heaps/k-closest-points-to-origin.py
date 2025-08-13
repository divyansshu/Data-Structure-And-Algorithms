import heapq

def kClosest(points, k):
    # Initialize a max heap (using negative distances)
    maxHeap = []
    for point in points:
        # Calculate squared distance from origin
        dist = point[0] * point[0] + point[1] * point[1]
        
        # If heap has less than k points, push current point
        if len(maxHeap) < k:
            heapq.heappush(maxHeap, (-dist, point))
        else:
            # If current point is closer than the farthest in heap
            if -dist > maxHeap[0][0]:
                # Remove the farthest point
                heapq.heappop(maxHeap)
                # Add the current point
                heapq.heappush(maxHeap, (-dist, point))
    # Extract only the points from the heap
    return [pair[1] for pair in maxHeap]

# Example usage
print(kClosest([[1,3],[-2,2]], k = 1))
print(kClosest([[3,3],[5,-1],[-2,4]], k = 2))