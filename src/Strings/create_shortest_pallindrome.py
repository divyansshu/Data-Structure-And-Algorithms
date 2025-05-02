'''
question link: https://leetcode.com/problems/shortest-palindrome/
'''


def shortestPalindrome(s):
    # If the string has length 1 or less, it is already a palindrome
    if len(s) <= 1: 
        return s
        
    # Create a new string by appending '#' and the reverse of the original string
    # This helps in finding the longest palindromic prefix using the LPS array
    new_s =  s + '#' + s[::-1]
    
    # Initialize the LPS (Longest Prefix Suffix) array for the new string
    lps = [0] * len(new_s)
    prevLps, i = 0, 1  # prevLps tracks the length of the previous LPS, i is the current index

    # Compute the LPS array for the new string
    while i < len(new_s):
        if new_s[i] == new_s[prevLps]:
            # If characters match, increment prevLps and set lps[i]
            lps[i] = prevLps + 1
            prevLps += 1
            i += 1
        elif prevLps == 0:
            # If no match and prevLps is 0, set lps[i] to 0 and move to the next character
            lps[i] = 0
            i += 1
        else:
            # If no match, reduce prevLps to the value of the previous LPS
            prevLps = lps[prevLps - 1]

    # Calculate the number of characters to add to the beginning of the string
    n = len(s) - lps[-1]
    if n > 0:
        # Add the reverse of the required characters to the beginning of the string
        res = s[-n:][::-1] + s
    else:
        # If no characters need to be added, return the original string
        return s
    return res    

# Test cases to verify the function
print(shortestPalindrome("abc"))        # Output: "cbabc"
print(shortestPalindrome("aacecaaaa"))  # Output: "aaaacecaaaa"
print(shortestPalindrome("abcd"))       # Output: "dcbabcd"
print(shortestPalindrome("race"))       # Output: "ecarace"
print(shortestPalindrome("aaa"))        # Output: "aaa"
print(shortestPalindrome("abac"))       # Output: "cabac"