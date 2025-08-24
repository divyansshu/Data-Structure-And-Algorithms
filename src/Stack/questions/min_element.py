class Solution:

    def __init__(self):
        self.st = []
        self.min_ele = -1
        # self.min_st = []
    # Add an element to the top of Stack
    def push(self, x):
        if self.st:
            if x <= self.min_ele:
                self.st.append(2 * x - self.min_ele)
                self.min_ele = x
            else:
                self.st.append(x)
        else:
            self.st.append(x)
            self.min_ele = x
        
    # Remove the top element from the Stack
    def pop(self):
        if self.st:
            if self.st[-1] < self.min_ele:
                self.min_ele = 2 * self.min_ele - self.st[-1]
                self.st.pop()
            else:
                self.st.pop()
        return

    # Returns top element of Stack
    def peek(self):
        if self.st:
            if self.st[-1] < self.min_ele:
                return self.min_ele
            else:
                return self.st[-1]
        return -1

    # Finds minimum element of Stack
    def getMin(self):
        return self.min_ele if self.st else -1
            
        
        
        
           
        