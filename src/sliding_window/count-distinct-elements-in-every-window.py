from collections import defaultdict

def countDistinct(arr, k):
    res = []  # List to store the result for each window
    n = len(arr)
    freq = defaultdict(int)  # Dictionary to store frequency of elements in current window

    # Initialize the frequency dictionary with the first window
    for i in range(k):
        freq[arr[i]] += 1
    res.append(len(freq))  # Add count of distinct elements in the first window
        
    # Slide the window
    for i in range(k, n):
        freq[arr[i]] += 1  # Add the new element to the window
        freq[arr[i-k]] -= 1  # Remove the element going out of the window
            
        if freq[arr[i-k]] == 0:
            del freq[arr[i-k]]  # Remove the element from dictionary if its count is zero
            
        res.append(len(freq))  # Add count of distinct elements in the current window
    return res

# Example usage
print(countDistinct([1, 2, 1, 3, 4, 2, 3], k = 4))
print(countDistinct([4, 1, 1], k = 2))
print(countDistinct([1, 1, 1, 1, 1], k = 3))