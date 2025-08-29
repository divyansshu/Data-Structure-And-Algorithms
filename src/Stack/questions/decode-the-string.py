def decodeString(s: str) -> str:
    num_st = []      # Stack to store numbers (repeat counts)
    char_st = []     # Stack to store characters and intermediate strings
    num_str = ''     # Temporary string to build multi-digit numbers

    for char in s:
        if char.isdigit():
            # Build the number (could be more than one digit)
            num_str += char
        elif char == '[':
            # Push the current number to num_st and reset num_str
            num_st.append(int(num_str))
            num_str = ''
            # Mark the start of a bracketed segment
            char_st.append(char)
        elif char == ']':
            # Pop characters until '[' is found to get the current segment
            chars = []
            while char_st[-1] != '[':
                chars.append(char_st.pop())
            char_st.pop()  # Remove the '['

            num = num_st.pop()  # Get the repeat count
            # Repeat the segment and push back to char_st
            segment = ''.join(reversed(chars)) * num
            char_st.append(segment)
        else:
            # Push regular characters to char_st
            char_st.append(char)
    # Join everything in char_st to get the final decoded string
    return ''.join(char_st)

print(decodeString("1[b]"))         # Output: b
print(decodeString("3[b2[ca]]"))   # Output: bcacabcacabcaca
print(decodeString("11[geeks]"))   # Output: geeksgeeksgeeksgeeksgeeksgeeksgeeksgeeksgeeksgeeksgeeks