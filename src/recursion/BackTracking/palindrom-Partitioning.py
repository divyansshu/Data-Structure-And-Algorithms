def isPal(s, l , r):
    # Check if the substring s[l:r+1] is a palindrome
    while l <= r:
        if s[l] != s[r]:  # If characters don't match, not a palindrome
            return False
        l += 1
        r -= 1
    return True  # All characters matched, it's a palindrome

def partition(s):
    res = []    # To store all possible palindrome partitions
    part = []   # Current partition being constructed

    def backtrack(i):
        # If we've reached the end of the string, add the current partition to results
        if i >= len(s):
            res.append(part[:])  # Make a copy of the current partition
            return
        
        # Try all possible substrings starting at index i
        for j in range(i, len(s)):
            if isPal(s, i, j):  # If substring s[i:j+1] is a palindrome
                part.append(s[i: j+1])  # Add substring to current partition
                backtrack(j+1)          # Recurse for the remaining substring
                part.pop()              # Backtrack and remove the last substring

    backtrack(0)  # Start backtracking from index 0
    return res

# print(partition("aab"))
print(partition("aaba"))