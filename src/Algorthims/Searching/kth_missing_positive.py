def find_Kth_Positive(arr, k):
    # Get the length of the array
    n = len(arr)
    # Convert array to set for O(1) lookups
    set_arr = set(arr)
    # List to store missing positive integers
    missing_values = []
    i = 1
    # Continue until we find k missing numbers
    while len(missing_values) < k:
        # If i is not in the array, it's missing
        if i not in set_arr:
            missing_values.append(i)
        i += 1
    # Return the k-th missing positive number
    return missing_values[-1]

def using_binary_search(arr, k):
    l = 0
    h = len(arr) - 1
    
    # Binary search to find the position where k-th missing number fits
    while l <= h:
        mid = (l + h) // 2
        # Number of missing numbers before arr[mid]
        missing_count = arr[mid] - (mid + 1)
        
        if missing_count < k:
            # Move right if not enough missing numbers yet
            l = mid + 1
        else:
            # Move left if too many missing numbers
            h = mid - 1
    # The k-th missing number is l + k
    return l + k            

# Example usage and output
print(find_Kth_Positive([2,3,4,7,11], 5))
print(find_Kth_Positive([1,2,3,4], 2))

print(using_binary_search([2,3,4,7,11], 5))
print(using_binary_search([1,2,3,4], 2))