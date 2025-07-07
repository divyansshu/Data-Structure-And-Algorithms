def search(txt, pat):
    n = len(txt)
    i = j = 0  # Initialize window pointers
    freq = {}  # Dictionary to store frequency of characters in pattern
    res = 0    # Result to store count of anagram occurrences

    # Build the frequency dictionary for the pattern
    for k in range(len(pat)):
        freq[txt[k]] = freq.get(txt[k], 0)+1
    count  = len(freq)  # Count of unique characters to be matched

    while j < n:
        # If current character is part of the pattern, decrease its count
        if txt[j] in freq:
            freq[txt[j]] -= 1
            
            if freq[txt[j]] == 0:
                count -= 1  # Character matched completely

        # If window size matches pattern length
        if j - i + 1 == len(pat):
            if count == 0:
                res += 1  # Found an anagram

            # Before sliding the window, restore the count of the outgoing character
            if txt[i] in freq:
                freq[txt[i]] += 1
                if freq[txt[i]] == 1:
                    count += 1  # Character no longer matched completely
            i += 1  # Slide the window
        j += 1  # Expand the window

    return res

print(search(txt = "forxxorfxdofr", pat = "for"))
print(search(txt = "aabaabaa", pat = "aaba"))