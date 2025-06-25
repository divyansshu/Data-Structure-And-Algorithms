# Python Program to count all subarrays with XOR equal to a given value K

def subarrayXor(arr, k):
    # Dictionary to store how many times each prefix XOR has occurred
    map = {}
    cnt = 0  # This will count the number of subarrays found
    prefXor = 0  # This will store the XOR of elements from the start up to the current position
    for val in arr:
        prefXor ^= val  # Update prefix XOR by including the current element

        # If there is a previous prefix XOR such that (prefix XOR) ^ k = current prefix XOR,
        # then the subarray between those two points has XOR = k
        cnt += map.get(prefXor ^ k, 0)

        # If the current prefix XOR itself is equal to k, it means the subarray from the start has XOR = k
        if prefXor == k:
            cnt += 1

        # Record the current prefix XOR in the dictionary
        map[prefXor] = map.get(prefXor, 0) + 1
    
    # Return the total number of subarrays found
    return cnt

# Example usage
print(subarrayXor([4,2,2,6,4], 6))  # Output: 4
print(subarrayXor([2,8,1,3,5,8,9,3,3,8], 8))  # Output: 5
