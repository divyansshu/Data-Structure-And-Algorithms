def longestUniqueSubstr(s):
    # Initialize the length of the longest substring
    longest = 0
    n = len(s)
    # Boolean array to keep track of visited characters (assuming lowercase a-z)
    visited = [False] * 26
    # Initialize left and right pointers for the sliding window
    r = l = 0
    while r < n:
        # If current character is already in the window, move left pointer to remove duplicates
        while visited[ord(s[r]) - ord('a')] == True:
            visited[ord(s[l]) - ord('a')] = False
            l += 1
                    
        # Mark current character as visited
        visited[ord(s[r]) - ord('a')] = True
        # Update the maximum length found so far
        longest = max(longest, (r-l+1))
        # Move right pointer to expand the window
        r += 1
    return longest

# Test cases
print(longestUniqueSubstr("geeksforgeeks"))  # Output: 7
print(longestUniqueSubstr("abcdefabcbb"))    # Output: 6
print(longestUniqueSubstr("aaa"))            # Output: 1