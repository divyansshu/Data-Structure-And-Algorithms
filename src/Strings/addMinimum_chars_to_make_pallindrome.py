'''
question link: https://www.geeksforgeeks.org/problems/minimum-characters-to-be-added-at-front-to-make-string-palindrome/1
'''

def minChar(s):
    # Reverse the input string
    rev_s = s[::-1]
    
    # Initialize variables for the LPS (Longest Prefix Suffix) computation
    prevLps, i = 0, 1
    
    # Create a new string by concatenating the original string, a separator, and the reversed string
    new_s = s + '#' + rev_s
    
    # Initialize the LPS array with zeros
    lps = [0] * len(new_s)
        
    # Compute the LPS array for the new string
    while i < len(new_s):
        if new_s[i] == new_s[prevLps]:
            # If characters match, increment the LPS value and move forward
            lps[i] = prevLps + 1
            prevLps += 1
            i += 1
        elif prevLps == 0:
            # If no match and prevLps is 0, set LPS value to 0 and move forward
            lps[i] = 0
            i += 1
        else:
            # If no match, backtrack to the previous LPS value
            prevLps = lps[prevLps - 1]
    
    # The number of characters to be added is the difference between the string length
    # and the last value in the LPS array
    n = len(s) - lps[-1]
    return n

# Test cases to check the function
print(minChar("abc"))        # Output: 2 (Add "cb" to make "abccba")
print(minChar("aacecaaaa"))  # Output: 2 (Add "aa" to make "aaaacecaaaa")
print(minChar("abcd"))       # Output: 3 (Add "dcb" to make "abcdcba")
print(minChar("race"))       # Output: 3 (Add "eca" to make "racecar")
print(minChar("aaa"))        # Output: 0 (Already a palindrome)
print(minChar("abac"))       # Output: 1 (Add "b" to make "abacaba")