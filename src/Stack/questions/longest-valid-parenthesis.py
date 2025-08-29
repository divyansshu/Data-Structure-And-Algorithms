def maxLength(s):
    # Initialize stack with -1 to handle base for valid substring
    st = [-1]
    maxlen = 0  # To store the maximum length found
    valid_len = 0  # To store the current valid length

    for i in range(len(s)):
        if s[i] == '(':
            # Push index of '(' onto stack
            st.append(i)
        else:
            # Pop the last index (matching '(' or base)
            st.pop()
            if st:
                # If stack is not empty, calculate valid length
                valid_len = i - st[-1]
                maxlen = max(valid_len, maxlen)
            else:
                # If stack is empty, push current index as base
                st.append(i)
    return maxlen

# Test cases
print(maxLength("((()"))     # Output: 2
print(maxLength(")()())"))   # Output: 4
print(maxLength("())()"))    # Output: 2