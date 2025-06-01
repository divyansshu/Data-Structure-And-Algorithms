def findKRotation_method1(arr):
    n = len(arr)
    # Iterate through the array to find the point of rotation
    for i in range(n - 1):
        # If the current element is greater than the next element, rotation point is found
        if arr[i] > arr[i+1]:
            return i+1
    # If no rotation point is found, the array is not rotated
    return 0     

def findKRotation_method2(arr):
    n = len(arr)
    left, right = 0, n - 1
    # If the array is already sorted, return 0
    if arr[left] <= arr[right]: return 0
    # Perform binary search to find the rotation point
    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the rotation point
        if mid > 0 and arr[mid] < arr[mid-1]: return mid
        elif mid < n-1 and arr[mid] > arr[mid + 1]: return mid+1
        # Adjust the search range based on the mid value
        elif arr[mid] <= arr[left]: right = mid - 1
        else: left = mid + 1
        
    # If no rotation point is found, the array is not rotated
    return 0     

# Test cases
print(findKRotation_method1([6, 9, 2, 4]))  # Output: 2
print(findKRotation_method2([6, 9, 2, 4]))  # Output: 2
print(findKRotation_method1([8, 10, 21, 31, 43, 45]))  # Output: 0
print(findKRotation_method2([8, 10, 21, 31, 43, 45]))  # Output: 0