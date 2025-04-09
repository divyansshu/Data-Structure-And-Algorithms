def isIsomorphic(s, t):
    # If the lengths of the two strings are not equal, they cannot be isomorphic
    if len(s) != len(t):
        return False
    
    # Dictionaries to map characters from s to t and vice versa
    s_to_t = {}
    t_to_s = {}
    
    # Iterate through characters of both strings simultaneously
    for char_s, char_t in zip(s, t):
        # Check if char_s is already mapped to a character in t
        if char_s in s_to_t:
            # If the mapping does not match char_t, the strings are not isomorphic
            if s_to_t[char_s] != char_t: 
                return False
        else:
            # Create a new mapping from char_s to char_t
            s_to_t[char_s] = char_t
        
        # Check if char_t is already mapped to a character in s
        if char_t in t_to_s:
            # If the mapping does not match char_s, the strings are not isomorphic
            if t_to_s[char_t] != char_s:
                return False
        else:
            # Create a new mapping from char_t to char_s
            t_to_s[char_t] = char_s
    
    # If all checks pass, the strings are isomorphic
    return True        

# Test the function with example strings
t = 'foo'
s = 'bar'
print('Is isomorphic: ', isIsomorphic(s, t))