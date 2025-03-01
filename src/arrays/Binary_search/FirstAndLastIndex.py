def binSearch(nums, target, startBias):
    left, right = 0, len(nums) - 1
    index = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            index = mid
            # If startBias is True, move to the left half to find the first occurrence
            if startBias:
                right = mid - 1
            # If startBias is False, move to the right half to find the last occurrence
            else:
                left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return index                        
               

def searchRange(nums, target):
    # Find the first occurrence of the target
    startIndex = binSearch(nums, target, True)
    # Find the last occurrence of the target
    lastIndex = binSearch(nums, target, False)
    return [startIndex, lastIndex]


# Test cases
print(searchRange([5,7,7,8,8,10],8))  # Output: [3, 4]
print(searchRange([5,7,7,8,8,10],6))  # Output: [-1, -1]
print(searchRange([6,6,6,6,6,6],6))   # Output: [0, 5]
print(searchRange([2,3,6,8,9],6))     # Output: [2, 2]
print(searchRange([], 0))             # Output: [-1, -1]