def nextPermutation(nums):
    n = len(nums)

    # Step 1: Find the largest index `pivot` such that nums[pivot] < nums[pivot + 1]
    pivot = -1
    for i in range(n-1, 0, -1):
        if nums[i-1] < nums[i]:
            pivot = i-1
            break
    
    # If no such index exists, the permutation is the last permutation, so reverse to get the first permutation
    if pivot == -1:
        nums.reverse()
        return
    
    # Step 2: Find the largest index `nextMaxIndex` greater than `pivot` such that nums[nextMaxIndex] > nums[pivot]
    nextMaxIndex = -1
    for i in range(n-1, pivot, -1):
        if nums[i] > nums[pivot]:
            nextMaxIndex = i
            break

    # Step 3: Swap the value of nums[pivot] with that of nums[nextMaxIndex]
    nums[pivot], nums[nextMaxIndex] = nums[nextMaxIndex], nums[pivot]
    
    # Step 4: Reverse the sequence from nums[pivot + 1] to the end of the list
    nums[pivot+1:] = reversed(nums[pivot+1:])
    

# Test cases
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]

nums2 = [3, 2, 1]
nextPermutation(nums2)
print(nums2)  # Output: [1, 2, 3]

nums3 = [1, 3, 5, 4, 2]
nextPermutation(nums3)
print(nums3)  # Output: [1, 4, 2, 3, 5]