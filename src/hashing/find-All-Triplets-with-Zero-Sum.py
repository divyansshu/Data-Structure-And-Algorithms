def findTriplets(arr):
    res = []  # List to store the resulting triplets (as indices)
    map = {}  # Dictionary to map array values to their indices
    n = len(arr)
    
    # Iterate through each pair (j, k) in the array
    for j in range(n):
        for k in range(j+1, n):
            val = -1 * (arr[j] + arr[k])  # The value needed to make the sum zero
            
            # If this value has been seen before, add all valid triplets
            if val in map:
                for i in map[val]:
                    res.append([i, j, k])  # Append the indices of the triplet
        
        # After j'th index is traversed
        # We can use it as i.
        # by adding the current value and its index to the map
        if arr[j] not in map:
            map[arr[j]] = []
        map[arr[j]].append(j)
    return res

# Test cases
print(findTriplets([0, -1, 2, -3, 1]))
print(findTriplets([1, -2, 1, 0, 5]))
print(findTriplets([2, 3, 1, 0, 5]))