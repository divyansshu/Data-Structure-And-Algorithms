def rotateStrings(s, goal):
    # Check if the lengths of the strings are different; if so, they cannot be rotations
    if len(s) != len(goal):
        return False

    # Create a copy of the original string to perform rotations
    s3 = s
    for i in range(len(s)):
        # Rotate the string by moving the first character to the end
        s3 = s3[1:] + s3[0]
        # Check if the rotated string matches the goal string
        if s3 == goal:
            return True
    # If no match is found after all rotations, return False
    return False

def rotateStrings_method2(s, goal):
    # Check if the lengths of the strings are equal and if the goal string
    # is a substring of the concatenated string (s + s)
    return len(s) == len(goal) and goal in s + s

# Test cases
print(rotateStrings('abcde', 'cdeab'))  # True, 'cdeab' is a rotation of 'abcde'
print(rotateStrings('abcde', 'abced'))  # False, 'abced' is not a rotation of 'abcde'

print(rotateStrings_method2('abcde', 'cdeab'))  # True, 'cdeab' is a rotation of 'abcde'
print(rotateStrings_method2('abcde', 'abced'))  # False, 'abced' is not a rotation of 'abcde'