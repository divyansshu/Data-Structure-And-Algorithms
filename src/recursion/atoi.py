def myAtoi(s):
    # Remove leading and trailing whitespace
    s = s.strip()
    if not s:
        return 0  # Return 0 if string is empty after stripping

    n = len(s)
    i = 0
    sign = 1

    # Check for sign at the beginning
    if s[0] == '-':
        sign = -1
        i += 1  # Move index past the sign
    elif s[0] == '+':
        i += 1  # Move index past the sign

    # Recursive function to build the integer from digits
    def backtrack(idx, num):
        # Base case: end of string or non-digit character
        if idx == n or not s[idx].isdigit():
            return num

        # Add current digit to the number
        num = num * 10 + int(s[idx])
        # Recurse to next character
        return backtrack(idx + 1, num)

    # Get the result and apply the sign
    result = backtrack(i, 0) * sign

    # Clamp the result to 32-bit signed integer range
    if result < -2**31:
        return -2**31
    if result > 2**31 - 1:
        return 2**31 - 1

    return result

# Test cases
print(myAtoi("42"))           # Output: 42
print(myAtoi(" -042"))        # Output: -42
print(myAtoi("1337c0d3"))     # Output: 1337
print(myAtoi("0-1"))          # Output: 0
print(myAtoi("words and 987"))# Output: 0