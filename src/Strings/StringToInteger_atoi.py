def myAtoi(s):
    # Remove leading and trailing whitespaces
    s = s.strip()
    if not s:  # If the string is empty after stripping, return 0
        return 0
    
    # Initialize variables
    sign = 1  # Default sign is positive
    result = 0  # To store the final integer value
    index = 0  # Pointer to traverse the string
    
    # Check for optional sign at the beginning
    if s[0] == '+':  # If the first character is '+', move to the next character
        index += 1
    elif s[0] == '-':  # If the first character is '-', set sign to negative and move to the next character
        sign = -1
        index += 1    
    
    # Convert the numeric part of the string to an integer
    while index < len(s) and s[index].isdigit():  # Continue while characters are digits
        result = result * 10 + int(s[index])  # Build the integer digit by digit
        index += 1
       
    # Apply the sign to the result
    result *= sign
        
    # Define integer limits for 32-bit signed integers
    INT_MIN = -2**31  # Minimum value: -2147483648
    INT_MAX = 2**31 - 1  # Maximum value: 2147483647
    
    # Clamp the result to the 32-bit integer range
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    
    # Return the final result
    return result
         
# Test cases to validate the function
print(myAtoi('42'))           # Output: 42
print(myAtoi('-042'))         # Output: -42
print(myAtoi('1337c0d3'))     # Output: 1337 (stops parsing at the first non-digit character)
print(myAtoi('0-1'))          # Output: 0 (stops parsing at the first non-digit character)
print(myAtoi('words and 987')) # Output: 0 (no valid number at the start)
print(myAtoi('00000123'))     # Output: 123 (leading zeros are ignored)
print(myAtoi(' -'))           # Output: 0 (no digits after the sign)
print(myAtoi('-s'))           # Output: 0 (no digits after the sign)