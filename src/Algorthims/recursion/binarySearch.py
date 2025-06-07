def search(arr, low, high, target):
    if low > high:
        return False
    
    mid = (low+high) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
    return search(arr, low ,high, target)
    
    
print(search([1,2,3,4,5,6],0,5,2))        
        