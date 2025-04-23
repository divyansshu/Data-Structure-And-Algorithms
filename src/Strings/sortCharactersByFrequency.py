def frequencySort(s):
    # Create a dictionary to store the frequency of each character in the string
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1  # Increment the count if the character is already in the dictionary
        else:
            freq[char] = 1  # Initialize the count to 1 if the character is not in the dictionary
    
    # Sort the dictionary by frequency in descending order and convert it back to a dictionary
    sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    
    # Build the result string by repeating each character based on its frequency
    result = []
    for key, value in sorted_freq.items():
        for i in range(value):  # Append the character 'value' times
            result.append(key)
    
    # Join the list of characters into a single string and return it
    return ''.join(result)

# Test cases
print(frequencySort("tree"))        # Output: "eert" or "eetr"
print(frequencySort("cccaaa"))      # Output: "cccaaa" or "aaaccc"
print(frequencySort("Aabb"))        # Output: "bbAa" or "bbaA"