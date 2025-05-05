'''
question link: https://leetcode.com/problems/h-index/description/
'''

def findH_index(citations):
    # Get the number of papers
    n = len(citations)
    
    # Create a frequency array to count the number of papers with a given citation count
    # freq[i] will store the number of papers with exactly i citations
    # freq[n] will store the number of papers with citations greater than n
    freq = [0] * (n+1)
        
    # Populate the frequency array
    i = 0
    while i < n:
        if citations[i] > n:
            # If citations are greater than n, count them in freq[n]
            freq[n] += 1
        else:
            # Otherwise, count them in their respective citation bucket
            freq[citations[i]] += 1
        i += 1
        
    # Calculate the H-index
    total = 0
    # Traverse the frequency array from the highest possible H-index (n) to 0
    for H in range(n, -1, -1):
        # Accumulate the total number of papers with at least H citations
        total += freq[H]
        # If the total number of papers with at least H citations is >= H, return H
        if total >= H:
            return H

# Test cases to verify the function
print(findH_index([3, 0, 6, 1, 5]))  # Output: 3
print(findH_index([5,5,5]))          # Output: 3
print(findH_index([0,0,0,0]))        # Output: 0
print(findH_index([1]))              # Output: 1
print(findH_index([10, 15, 12, 5]))  # Output: 4
print(findH_index([1, 2, 3, 4, 5]))  # Output: 3
print(findH_index([7, 8, 9, 10]))    # Output: 4
print(findH_index([]))               # Output: 0