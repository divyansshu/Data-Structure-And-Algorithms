def checkValidGrid(grid):
    n = len(grid)
    def isValid(r, c, expVal):
        if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != expVal:
            return False
        if expVal == (n*n -1):
            return True
        ans1 = isValid(r-2, c+1, expVal+1) 
        ans2 = isValid(r-2, c-1, expVal+1) 
        ans3 = isValid(r+1, c+2, expVal+1) 
        ans4 = isValid(r-1, c+2, expVal+1) 
        ans5 = isValid(r+2, c+1, expVal+1) 
        ans6 = isValid(r+2, c-1, expVal+1) 
        ans7 = isValid(r-1, c-2, expVal+1) 
        ans8 = isValid(r+1, c-2, expVal+1)

        return ans1 or ans2 or ans3 or ans4 or ans5 or ans6 or ans7 or ans8
    return isValid(0,0, 0)

print(checkValidGrid([[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]))
print(checkValidGrid([[0,3,6],[5,8,1],[2,7,4]]))
             
        