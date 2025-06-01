def sort(arr):
    n = len(arr)
    gap = n // 2  # Initialize the gap size

    # Reduce the gap until it becomes 0
    while gap > 0:
        # Perform a gapped insertion sort for this gap size
        for i in range(gap, n):
            temp = arr[i]  # Store the current element
            j = i
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp  # Place temp at its correct location
        gap //= 2  # Reduce the gap for the next iteration
    print(arr)  # Print the sorted array

sort([23,29,15,19,31,7,9,5,2])