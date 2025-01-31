'''
time complexity: three nested loops
                = O(n^3)
space complexity: O(1)                 
'''
def threeSum(nums):
    n = len(nums)  # Get the length of the input list
    triplets = []  # Initialize an empty list to store the triplets

    # Iterate through each element in the list
    for i in range(n):
        # Iterate through each element after the current element
        for j in range(i+1, n):
            # Iterate through each element after the second element
            for k in range(j+1, n):
                # Check if the sum of the three elements is zero
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort the triplet to avoid duplicates
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    
                    # Add the triplet to the list if it's not already present
                    if triplet not in triplets:
                        triplets.append(triplet)               

    # Print the list of triplets
    print(triplets)       
    
'''
time complexity: sorting + two pointers
                 O(nlogn) + O(n^2) = O(n^2)
space complexity: O(1)                 
'''
def threeSum_method2(nums):
    # Sort the input list to make it easier to avoid duplicates and use two-pointer technique
    nums.sort()
    n = len(nums)
    result = []
    
    # Iterate through each element in the list
    for i in range(n-2):
        
        # Skip duplicate elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Initialize two pointers
        left, right = i+1, n-1
        
        # Use two-pointer technique to find triplets
        while left < right:
            
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                # If the sum is zero, add the triplet to the result list
                result.append([nums[i], nums[left], nums[right]])
                
                # Move the left pointer to the right and right pointer to the left
                left += 1
                right -= 1
                
                # Skip duplicate elements to avoid duplicate triplets
                while left < right and nums[left] == nums[left - 1]: left += 1
                while left < right and nums[right] == nums[right + 1]: right -= 1
                
            elif total < 0:
                # If the sum is less than zero, move the left pointer to the right
                left += 1
            else:
                # If the sum is greater than zero, move the right pointer to the left
                right -= 1
    
    # Print the list of triplets
    print(result)
                          

# Call the function with a sample input
threeSum([-1,0,1,2,-1,-4])    
threeSum_method2([-1,0,1,2,-1,-4])    
