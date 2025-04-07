arr = [1, 2, 0, 4, 3, 0, 5, 0]

def moveZeroesToEnd(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr        
            
print(moveZeroesToEnd(arr))            