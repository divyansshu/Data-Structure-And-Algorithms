def next_gap(gap):
    # Helper function to calculate the next gap value
    # If gap is 1 or less, return 0 to end the process
    # Otherwise, return the ceiling of gap/2
    if gap <= 1:
        return 0
    return (gap+1) // 2

def mergeArrays(a, b):
    n = len(a)
    m = len(b)
    gap = next_gap(n + m)  # Initial gap is the combined length of both arrays

    # Continue looping until gap becomes 0
    while gap > 0:
        i = 0
        j = gap
        # Compare and swap elements with 'gap' distance apart
        while j < n + m:
            # Both pointers in array 'a'
            if i < n and j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
            # i in 'a', j in 'b'
            elif i < n and j >= n:
                if a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]
            # Both pointers in array 'b'
            elif i >= n:
                if b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]
            i += 1
            j += 1

        # Update the gap for the next iteration
        gap = next_gap(gap)

    # Print the merged arrays (sorted in-place)
    print(a)
    print(b)

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
mergeArrays(a, b)