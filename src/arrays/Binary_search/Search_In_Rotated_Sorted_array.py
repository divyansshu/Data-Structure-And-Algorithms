
# Search_In_Rotated_Sorted_array:

    #find the pivot element
def pivot(arr):
    start = 0
    end = len(arr) - 1

    while start <= end :
        
        mid = (start + end) // 2

        # case 1
        if mid < end and arr[mid] > arr[mid+1]: return mid
            
        # case 2
        elif mid > start and arr[mid] < arr[mid-1]: return mid-1

        # case 3
        elif arr[mid] <= arr[start]:
            end = mid - 1
        
        # case 4
        else:  #arr[mid] >= arr[start]
            start = mid + 1
    return -1


def search(arr, key):
    
    Pivot = pivot(arr)

    # case1: 
    # array is not rotated, just do normal binary search
    if Pivot == -1:
        return binarySearch(arr, key, 0, len(arr) - 1)

    # case2:
    elif arr[Pivot] == key: return Pivot
             
    # case3:
    # if pivot is not -1
    elif arr[0] > key: 
        return binarySearch(arr, key, Pivot + 1, len(arr) - 1)
    
    # case4:
    # if key > arr[0]
    else:  
        return binarySearch(arr,key, 0, Pivot - 1)


def binarySearch(arr, key, start, end): 
    
    while start <= end: 
        mid = (start + end) // 2
        
        if arr[mid] == key: return 1
        
        elif key > arr[mid]: start = mid + 1
        
        else:  end = mid - 1
    return -1

nums = [3, 5, 6, 0, 1, 2]
print(search(nums, 9))