def rearrangeArray(nums):
    # Initialize the result array with zeros, same length as input array
    result = [0] * len(nums)
    
    # Initialize two lists to hold positive and negative numbers separately
    positive = []
    negative = []
    
    # Iterate through the input array and separate positive and negative numbers
    for i in range(len(nums)):
        if nums[i] > 0: 
            positive.append(nums[i])
        else:
            negative.append(nums[i])
    
    # Initialize pointers for the result array and the positive/negative lists
    j = 0
    k = 0
    
    # Alternate placing positive and negative numbers in the result array
    while j < len(positive) + len(negative):
        result[j] = positive[k]  # Place positive number
        j += 1
        result[j] = negative[k]  # Place negative number
        k += 1
        j += 1
    
    # Print the rearranged array
    print(result)    
    
# Example usage
nums = [3,1,-2,-5,2,-4]   
rearrangeArray(nums) 