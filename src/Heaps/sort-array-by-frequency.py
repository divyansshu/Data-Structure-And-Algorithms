import heapq

def sortByFreq(arr):
    # Create a frequency map to count occurrences of each number
    mp = {}
    for num in arr:
        mp[num] = mp.get(num, 0) + 1

    # Build a max-heap based on frequency (use negative frequency for max-heap)
    max_heap = [(-mp[num], num) for num in mp]
    heapq.heapify(max_heap)

    res = []
    # Extract elements from heap and add them to result based on their frequency
    while len(max_heap) > 0:
        freq, key = heapq.heappop(max_heap)
        # Append the number 'key' '-freq' times to the result list
        for i in range(-freq):
            res.append(key)
    return res

# Example usages
print(sortByFreq([1,1,2,2,2,3]))
print(sortByFreq([2,3,1,3,2]))
print(sortByFreq([-1,1,-6,4,5,-6,1,4,1]))