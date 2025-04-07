'''
time complexity: O(n * k)
space complexity: O(1)
'''
def rotate_method_1(arr, k):
    n = len(arr)
    
    # Rotate the array k times
    for _ in range(k):
        # Store the last element in a temporary variable
        temp = arr[n-1]
        
        # Shift all elements to the right by one position
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        # Place the last element at the first position
        arr[0] = temp


'''
time complexity: O(n)
space complexity: O(1)
'''
def rotate_method_2(nums, k):
    n = len(nums)
    
    # Reverse the entire array
    nums.reverse()
    
    # Ensure k is within the bounds of the array length
    k %= n
    
    # Reverse the first k elements
    nums[:k] = reversed(nums[:k])
    # Reverse the remaining elements
    nums[k:] = reversed(nums[k:])
    
# Example usage
nums = [1,2,3,4,5,6]
print('Array before rotation')
print(nums)

# Rotate the array by 3 positions using rotate_method_2
rotate_method_2(nums, 3)
print('Array after rotation')
print(nums)            