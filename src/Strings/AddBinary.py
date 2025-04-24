#
#  * This implementation handles binary addition directly on the strings and
#  * avoids potential issues with integer overflow.
#  * time complexity: O(n)
#  * space complexity: O(n)
#  
def addBinary(s1, s2):
    # Initialize pointers for the end of both strings
    i = len(s1) - 1
    j = len(s2) - 1
    # Initialize carry to handle overflow during addition
    carry = 0
    # Initialize a list to store the result in reverse order
    result = []

    # Loop until all bits are processed or there is a carry left
    while i >= 0 or j >= 0 or carry != 0:
        # Get the current bit from s1, or 0 if out of bounds
        bit1 = int(s1[i]) if i >= 0 else 0
        # Get the current bit from s2, or 0 if out of bounds
        bit2 = int(s2[j]) if j >= 0 else 0

        # Calculate the sum of the two bits and the carry
        bit_sum = bit1 + bit2 + carry
        # Append the least significant bit of the sum to the result
        result.append(str(bit_sum % 2))
        # Update the carry for the next iteration
        carry = bit_sum // 2
        # Move to the previous bit in both strings
        i -= 1
        j -= 1
    
    # Reverse the result list, join it into a string, and remove leading zeros
    result = ''.join(reversed(result)).lstrip('0')
    # Return the result, or '0' if the result is empty
    return result if result else '0'


# Example usage
s1 = '00100'
s2 = '010'
print(addBinary(s1, s2))
