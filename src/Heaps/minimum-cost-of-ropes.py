import heapq

def minCost(arr):
    # Create a min-heap from the input array
    min_heap = [num for num in arr]
    heapq.heapify(min_heap)
       
    totalCost = 0  # Initialize total cost to 0
    # Continue until only one rope remains
    while len(min_heap) > 1:
        # Extract the two smallest ropes
        num1 = heapq.heappop(min_heap)
        num2 = heapq.heappop(min_heap)
        # Combine them (cost is their sum)
        cost = num1 + num2
        totalCost += cost  # Add the cost to total
        # Push the combined rope back into the heap
        heapq.heappush(min_heap, cost)
    return totalCost  # Return the minimum total cost

# Example usage
print(minCost([4, 3, 2, 6]))        # Output: 29
print(minCost([4, 2, 7, 6, 9]))     # Output: 62