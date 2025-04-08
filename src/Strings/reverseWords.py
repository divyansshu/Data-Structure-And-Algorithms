def reverseWords(s: str) -> str:
    # Split the input string into a list of words using whitespace as the delimiter
    words = s.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join the reversed list of words back into a single string with spaces in between
    return ' '.join(reversed_words)
     
# Input string
s = "a good example"

# Call the function and print the result
print(reverseWords(s))
