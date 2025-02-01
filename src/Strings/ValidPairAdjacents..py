from collections import Counter

def findValidPair(s):
    # Get the length of the string
    n = len(s)
    
    # Create a frequency counter for the characters in the string
    freq = Counter(s)
    
    # Iterate through the string, stopping one character before the end
    for i in range(n-1):
        # Get the current character and the next character
        num1, num2 = s[i], s[i+1]
        
        # Check if the current character is different from the next character
        if num1 != num2:
            # Check if the frequency of both characters matches their integer value
            if freq[num1] == int(num1) and freq[num2] == int(num2):
                # Return the concatenation of the two characters
                return num1 + num2
    
    # If no valid pair is found, return an empty string
    return ""

# Test cases
print(findValidPair("234233"))  # Expected output: "23"
print(findValidPair("22"))      # Expected output: ""