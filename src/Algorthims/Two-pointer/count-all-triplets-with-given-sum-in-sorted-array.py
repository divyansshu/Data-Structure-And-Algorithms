def countTriplets(arr, target):
    n = len(arr)
    res = 0
    # Iterate through each element, fixing the first element of the triplet
    for i in range(n-2):
        left = i+1
        right = n-1   
        # Use two pointers to find pairs that sum with arr[i] to target
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum < target:
                # If sum is less than target, move left pointer to increase sum
                left += 1
            elif sum > target:
                # If sum is greater than target, move right pointer to decrease sum
                right -= 1
            else:
                # If sum matches target, count duplicates for left and right
                left_ele = arr[left]
                right_ele = arr[right]
                left_cnt = 0
                right_cnt = 0
                # Count occurrences of arr[left]
                while left <= right and arr[left] == left_ele:
                    left += 1
                    left_cnt += 1
                # Count occurrences of arr[right]
                while left <= right and arr[right] == right_ele:
                    right -= 1
                    right_cnt += 1
                
                if left_ele == right_ele:
                    # If both pointers point to the same value, count combinations
                    res += (left_cnt * (left_cnt-1)) // 2
                else:
                    # Otherwise, multiply the counts for left and right values
                    res += (left_cnt * right_cnt)           
    return res

# Example usage
print(countTriplets([-3, -1, -1, 0, 1, 2], target = -2))
print(countTriplets([-2, 0, 1, 1, 5], target = 1))
print(countTriplets([1,1,1,1,1,1], 3))