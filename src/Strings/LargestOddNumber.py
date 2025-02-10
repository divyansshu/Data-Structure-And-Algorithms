def largestOddNumber(nums):
    # Initialize an empty string to store the largest odd number
    maxOdd = ""
    
    # Iterate over the string from the end to the beginning
    for i in range(len(nums)-1, -1, -1):
        # Check if the current character is an even number
        if int(nums[i]) % 2 == 0:
            continue  # If it's even, skip to the next iteration
        else:
            # If it's odd, slice the string up to the current index (inclusive)
            maxOdd = nums[:i+1]
            break  # Break the loop as we found the largest odd number
    
    return maxOdd  # Return the largest odd number

# Test cases
print(largestOddNumber('4206'))  # Output: ""
print(largestOddNumber('35427'))  # Output: "35427"
print(largestOddNumber('5234'))  # Output: "523"