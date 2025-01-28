from functools import cmp_to_key

# Custom comparator function to decide the order of numbers
def compare(a, b):
    # Compare concatenated strings in both possible orders
    if a + b > b + a: 
        return -1  # a should come before b
    elif b + a > a + b: 
        return 1   # b should come before a
    else: 
        return 0   # a and b are equal in terms of order

# Function to form the largest number from a list of non-negative integers
def largestNumber(nums):
    # Convert all integers to strings for easy concatenation and comparison
    arr = [str(num) for num in nums]
    
    # Sort the array using the custom comparator
    arr.sort(key=cmp_to_key(compare))
    
    # If the largest number is '0', the result is '0' (to handle cases like [0, 0])
    if arr[0] == '0': 
        return '0'
    
    # Join the sorted array to form the largest number
    return ''.join(arr)
    
# Example usage
arr = [10, 2, 9, 39, 17]
print(largestNumber(arr))  # Output: 93921710