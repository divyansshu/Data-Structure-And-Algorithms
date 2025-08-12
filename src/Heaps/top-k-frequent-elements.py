import heapq

def topkFrequent(nums, k):
    # Create a frequency map to count occurrences of each number
    mp = {}
    for num in nums:
        mp[num] = mp.get(num, 0) + 1

    # Build a max-heap using negative frequencies (since heapq is a min-heap by default)
    max_heap = [(-mp[num], num) for num in mp]
    heapq.heapify(max_heap)

    res = []
    # Extract the top k elements with highest frequency
    for _ in range(k):
        _, val = heapq.heappop(max_heap)
        res.append(val)
    return res

# Example usage
print(topkFrequent([1,1,1,2,2,3], k = 2))  # Output: [1, 2]
print(topkFrequent([1], k = 1))            # Output: [1]