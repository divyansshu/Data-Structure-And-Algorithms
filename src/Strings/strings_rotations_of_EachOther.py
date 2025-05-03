'''
question link: https://leetcode.com/problems/rotate-string/description/
'''


# Function to compute the Longest Prefix Suffix (LPS) array for the KMP algorithm
def compute_lps(s2):
    lps = [0] * len(s2)  # Initialize LPS array with zeros
    prevLps, i = 0, 1  # prevLps tracks the length of the previous LPS, i is the current index

    while i < len(s2):
        if s2[i] == s2[prevLps]:  # If characters match
            lps[i] = prevLps + 1  # Update LPS value
            prevLps += 1  # Move prevLps forward
            i += 1  # Move to the next character
        elif prevLps == 0:  # If no prefix matches
            lps[i] = 0  # Set LPS value to 0
            i += 1  # Move to the next character
        else:  # If characters don't match and prevLps > 0
            prevLps = lps[prevLps - 1]  # Move prevLps back to the previous LPS value

    return lps  # Return the computed LPS array


# Function to check if two strings are rotations of each other using the KMP algorithm
def areRotations_using_kmp_algo(s1, s2):
    new_s = s1 + s1  # Concatenate the string with itself
    lps = compute_lps(s2)  # Compute the LPS array for s2
    i = 0  # Pointer for new_s
    j = 0  # Pointer for s2

    while i < len(new_s):
        if new_s[i] == s2[j]:  # If characters match
            i += 1  # Move both pointers forward
            j += 1
        else:
            if j == 0:  # If no match and j is at the start
                i += 1  # Move i forward
            else:  # If no match and j > 0
                j = lps[j - 1]  # Use LPS to skip unnecessary comparisons

        if j == len(s2):  # If all characters of s2 are matched
            return True  # s2 is a rotation of s1

    return False  # s2 is not a rotation of s1


# Test cases for the KMP-based rotation check
print(areRotations_using_kmp_algo("abcd", "cdab"))  # True
print(areRotations_using_kmp_algo("aab", "aba"))    # False
print(areRotations_using_kmp_algo("abcd", "acbd"))  # False
print(areRotations_using_kmp_algo("abcde", "cdeab"))  # True
print(areRotations_using_kmp_algo("abcde", "abced"))  # False


# Function to check if two strings are rotations of each other using the 'in' operator
def areRotations_using_in(s1, s2):
    new_s = s1 + s1  # Concatenate the string with itself
    return s2 in new_s  # Check if s2 is a substring of the concatenated string


# Test cases for the 'in'-based rotation check
print('\n')
print(areRotations_using_in("abcd", "cdab"))  # True
print(areRotations_using_in("aab", "aba"))    # False
print(areRotations_using_in("abcd", "acbd"))  # False
print(areRotations_using_in("abcde", "cdeab"))  # True
print(areRotations_using_in("abcde", "abced"))  # False

