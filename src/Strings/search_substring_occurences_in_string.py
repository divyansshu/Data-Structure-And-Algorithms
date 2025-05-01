def search_naive_method(txt, pat):
  # Get the lengths of the text and the pattern
  n1 = len(txt)
  n2 = len(pat)
  # Initialize an empty list to store the starting indices of matches
  res = []
    
  # Loop through the text, stopping at a point where the remaining substring
  # is shorter than the pattern
  for i in range(n1 - n2 + 1):
    match = True  # Assume a match initially
    # Check each character of the pattern against the corresponding character in the text
    for j in range(n2):
      if txt[i+j] != pat[j]:  # If characters don't match
        match = False  # Set match to False
        break  # Exit the inner loop
    if match:  # If a match is found
      res.append(i)  # Append the starting index of the match to the result list
  return res  # Return the list of starting indices



def compute_lps(pat):
  # Initialize the LPS (Longest Prefix Suffix) array with zeros
  lps = [0] * len(pat)
  prevLps, i = 0, 1  # prevLps tracks the length of the previous LPS, i is the current index

  # Build the LPS array
  while i < len(pat):
    if pat[i] == pat[prevLps]:  # If characters match
      lps[i] = prevLps + 1  # Update the LPS value
      prevLps += 1  # Move to the next prefix
      i += 1  # Move to the next character
    elif prevLps == 0:  # If no prefix matches
      lps[i] = 0  # Set LPS value to 0
      i += 1  # Move to the next character
    else:  # If there is a mismatch, but prevLps > 0
      prevLps = lps[prevLps - 1]  # Fall back to the previous LPS value

  return lps  # Return the computed LPS array


def search_using_kmp_algo(txt, pat):
  # Compute the LPS array for the pattern
  lps = compute_lps(pat)
  i = 0  # Pointer for the text
  j = 0  # Pointer for the pattern
  res = []  # List to store the starting indices of matches

  # Traverse the text
  while i < len(txt):
    if txt[i] == pat[j]:  # If characters match
      i += 1  # Move both pointers forward
      j += 1
    else:
      if j == 0:  # If no match and j is at the start of the pattern
        i += 1  # Move the text pointer forward
      else:  # If no match but j > 0
        j = lps[j - 1]  # Use the LPS array to skip unnecessary comparisons

    if j == len(pat):  # If the entire pattern is matched
      res.append(i - len(pat))  # Append the starting index of the match
      j = lps[j - 1]  # Reset j using the LPS array to find subsequent matches

  return res  # Return the list of starting indices
                


print('using naive method in O(m*n) time complexity')
print(search_naive_method("abcab", "ab"))  # Output: [0, 3]
print(search_naive_method("abesdu", "edu"))  # Output: []
print(search_naive_method("aabaacaadaabaaba", "aaba"))  # Output: [0, 9, 12]
print(search_naive_method("ABABABA", "ABA"))  # Output: [0, 2, 4]
print(search_naive_method("AAAAA", "AAA"))  # Output: [0, 1, 2]




print('using knuth-morris-pratt algo method in O(m+n) time complexity')
print(search_using_kmp_algo("abcab", "ab"))  # Output: [0, 3]
print(search_using_kmp_algo("abesdu", "edu"))  # Output: []
print(search_using_kmp_algo("aabaacaadaabaaba", "aaba"))  # Output: [0, 9, 12]
print(search_using_kmp_algo("ABABABA", "ABA"))  # Output: [0, 2, 4]
print(search_using_kmp_algo("AAAAA", "AAA"))  # Output: [0, 1, 2]