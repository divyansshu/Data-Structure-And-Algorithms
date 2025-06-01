def findPeakGrid(mat):
    rows, cols = len(mat), len(mat[0])
    
    i = 0
    for row in mat:
        left, right = 0, cols - 1
        while left < right:
            mid = (left + right) // 2
            if (mid == cols - 1 or row[mid] > row[mid + 1]) and (mid == 0 or row[mid] > row[mid - 1]): 
                if (i == 0 or row[mid] > mat[i-1][mid]) and (i == rows - 1 or row[mid] > mat[i+1][mid]):
                    return [i, mid]
            elif mid > 0 and row[mid-1] > row[mid]:
                right = mid - 1
            else:
                left = mid + 1
        i+=1        
    return [-1,-1]

print(findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))                 