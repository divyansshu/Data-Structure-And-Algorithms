def beautySum(s):
    n = len(s)  # Length of the input string
    subStr = []  # List to store all substrings of length >= 3

    # Generate all substrings of length >= 3
    for i in range(n):
        j = i
        for k in range(n):
            # Check if the substring of length >= 3 can be formed
            if (3 + j + k) <= n:
                subStr.append(s[i: 3+j+k])  # Append the substring to the list
            else:
                break  # Exit the loop if the substring exceeds the string length

    sum = 0  # Variable to store the sum of beauty values of all substrings

    # Calculate the beauty value for each substring
    for sub in subStr:
        freq = {}  # Dictionary to store the frequency of each character in the substring

        # Count the frequency of each character in the substring
        for i in range(len(sub)):
            if sub[i] in freq:
                freq[sub[i]] += 1
            else:
                freq[sub[i]] = 1

        # Sort the frequency values to find the maximum and minimum frequencies
        sorted_freq = sorted(freq.values())
        sum += sorted_freq[-1] - sorted_freq[0]  # Add the difference between max and min frequencies to the sum

    return sum  # Return the total beauty sum

# Example usage
print(beautySum('aabcbaa'))  # Output is 17 - 