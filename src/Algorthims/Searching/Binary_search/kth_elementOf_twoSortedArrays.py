def kthElement_merge_approach(a, b, k):
    n, m = len(a), len(b)
    i = j = 0
    # Traverse both arrays using two pointers
    while i < n and j < m:
        # Compare current elements of both arrays
        if a[i] < b[j]:
            # If k-th element is found, return it
            if k - 1 == 0:
                return a[i]
            i += 1  # Move pointer in array a
        else:
            if k - 1 == 0:
                return b[j]
            j += 1  # Move pointer in array b
        k -= 1  # Decrement k as one element is considered

    # If elements remain in array a
    while i < n:
        if k - 1 == 0:
            return a[i]
        i += 1
        k -= 1

    # If elements remain in array b
    while j < m:
        if k - 1 == 0:
            return b[j]
        j += 1
        k -= 1

# Example usage:
print(kthElement_merge_approach(a=[2, 3, 6, 7, 9], b=[1, 4, 8, 10], k=5))
print(kthElement_merge_approach(a=[100, 112, 256, 349, 770], b=[72, 86, 113, 119, 265, 445, 892], k=7))
