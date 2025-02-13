from collections import deque

# Brute force approach to find the next greater element
def nextGreaterElement_bruteForce(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    result = []
    index = -1
    
    # Iterate through each element in nums1
    for i in range(n1):
        num = nums1[i]
        # Find the index of the current element in nums2
        for j in range(n2):
            if num == nums2[j]:
                index = j
                break
             
        # Find the next greater element in nums2 starting from the found index
        for k in range(index, n2 - 1):
            if (nums2[index+1] > num):
                result.append(nums2[index+1])
                break
            else: 
                index += 1
            
        # If no greater element is found, append -1
        if index == n2 - 1:
            result.append(-1)     
    return result

# Optimized approach to find the next greater element using a stack
'''
time complexity: O(n + m)
space complexity: O(m)
'''
def nextGreaterElement_optimized(nums1, nums2):
    stack = deque()
    nge_map = {}
    
    # Iterate through each element in nums2
    for num in nums2:
        # Maintain a decreasing stack and map the next greater element
        while stack and stack[-1] < num:
            nge_map[stack.pop()] = num
        stack.append(num)
    
    # For remaining elements in the stack, there is no greater element
    while stack:
        nge_map[stack.pop()] = -1
    
    # Map the results for nums1 based on the precomputed map
    return [nge_map[num] for num in nums1]            
    

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement_bruteForce(nums1, nums2))            
print(nextGreaterElement_optimized(nums1, nums2))            