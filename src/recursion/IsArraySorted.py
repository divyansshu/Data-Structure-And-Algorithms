def isSorted(arr, i, n):
    if i == n - 1:
        return True
    
    if arr[i] <= arr[i+1]: 
        return isSorted(arr, i+1, n)
    else:
        return False
    
print(isSorted([1,2,3,4,5], 0, 5))    
print(isSorted([1,2,8,4,5], 0, 5))    