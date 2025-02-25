def countReversePairs(nums):
    # Helper function to perform merge sort and count reverse pairs
    def mergeSort(nums, left, right):
        # Base case: if the subarray has one or no elements, no reverse pairs
        if left >= right: return 0
        
        # Find the middle point to divide the array into two halves
        mid = (left + right) // 2
        
        # Recursively count reverse pairs in the left and right halves
        count = mergeSort(nums, left, mid) + mergeSort(nums, mid + 1, right)
        
        # Count the reverse pairs where one element is in the left half and the other is in the right half
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))
        
        # Merge the two halves while sorting them
        merge(nums, left, mid, right)
        return count
    
    # Helper function to merge two sorted halves of the array
    def merge(nums, left, mid, right):
        i, j = left, mid + 1
        sortedArr = []        
        
        # Merge the two halves into a sorted array
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                sortedArr.append(nums[i])
                i += 1
            else:
                sortedArr.append(nums[j])
                j += 1
        while i <= mid:
            sortedArr.append(nums[i])
            i += 1
        while j <= right:
            sortedArr.append(nums[j])
            j += 1
        
        # Copy the sorted array back to the original array
        nums[left:right+1] = sortedArr    
                    
    # Call the mergeSort function and return the count of reverse pairs
    return mergeSort(nums, 0, len(nums) - 1)

# Test cases
print(countReversePairs([1, 3, 2, 3, 1]))  # Output: 2
print(countReversePairs([2, 4, 3, 5, 1]))  # Output: 3