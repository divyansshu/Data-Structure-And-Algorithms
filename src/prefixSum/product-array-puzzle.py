def productExceptSelf(arr):
    n = len(arr)
    Product = 1  # To store the product of all non-zero elements
    zeroCnt = 0  # To count the number of zeros in the array
    result = [0] * n  # Initialize result array with zeros
    idx = -1  # To store the index of zero if there is exactly one zero
        
    # Calculate product of all non-zero elements and count zeros
    for i in range(n):
        if arr[i] != 0:
            Product *= arr[i]
        else:
            idx = i
            zeroCnt += 1
        
    # If there are no zeros, each result[i] is total product divided by arr[i]
    if zeroCnt == 0:
        for i in range(n):
            result[i] = Product // arr[i]
        
    # If there is exactly one zero, only the position with zero gets the product, rest remain zero
    elif zeroCnt == 1:
        result[idx] = Product
            
    # If more than one zero, all products will be zero (already initialized)
    return result

print(productExceptSelf([10, 3, 5, 6, 2]))
print(productExceptSelf([12, 0]))