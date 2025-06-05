def findMedianSortedArrays(nums1, nums2):
    # Get lengths of both arrays
    n = len(nums1)
    m = len(nums2)
    total = (n + m)  # Total number of elements
    half = total // 2  # Halfway point

    # Ensure nums1 is the smaller array for binary search efficiency
    if n > m:
        nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)

    low = 0
    high = n - 1

    while True:
        # Partition nums1
        mid1 = (low + high) // 2
        # Partition nums2 so that left parts together have 'half' elements
        mid2 = half - mid1 - 2

        # Get left and right values around the partition for both arrays
        l1 = nums1[mid1] if mid1 >= 0 else float('-infinity')
        r1 = nums1[mid1+1] if (mid1 + 1) < n else float('infinity')
        l2 = nums2[mid2] if mid2 >= 0 else float('-infinity')
        r2 = nums2[mid2+1] if (mid2 + 1) < m else float('infinity')

        # Check if correct partition is found
        if l1 <= r2 and l2 <= r1:
            # If total number of elements is odd, return the minimum of right elements
            if total % 2 == 1:
                return min(r1, r2)
            # If even, return the average of the max left and min right
            return (max(l1, l2) + min(r1, r2)) / 2
        # If l1 is too big, move partition in nums1 to the left
        elif l1 > r2:
            high = mid1 - 1
        # If l2 is too big, move partition in nums1 to the right
        else:
            low = mid1 + 1     
    return 0.0  # Should never reach here

# Example usage
print(findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))