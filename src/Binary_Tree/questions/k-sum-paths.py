class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None
        
from collections import deque

def buildTree(nodes):
    # Builds a binary tree from a list of values (level order)
    if not nodes or nodes[0] is None:
        return None
    
    root = Node(nodes[0])
    q = deque([root])
    i = 1
    
    while q and i < len(nodes):
        node = q.popleft()
        
        # Assign left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = Node(nodes[i])
            q.append(node.left)
        i += 1
        
        # Assign right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = Node(nodes[i])
            q.append(node.right)
        i += 1        
    return root

def printTree(root):
    # Preorder traversal to print the tree
    if root is None:
        return None
    
    print(root.data, end=' ')
    printTree(root.left)
    printTree(root.right)
    
def countPaths(node, k, curSum, prefixSum):
    # Counts the number of paths with sum k using prefix sum technique
    if node is None:
        return 0
    
    pathCount = 0
    curSum += node.data  # Update current path sum
    
    # If current sum equals k, increment path count
    if curSum == k:
        pathCount += 1
    
    # Add the number of times (curSum - k) has occurred to pathCount
    pathCount += prefixSum.get(curSum - k, 0)
    
    # Update prefixSum for current sum
    prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
    
    # Recurse for left and right subtrees
    pathCount += countPaths(node.left, k, curSum, prefixSum)
    pathCount += countPaths(node.right, k, curSum, prefixSum)
    
    # Remove current sum from prefixSum to backtrack
    prefixSum[curSum] -= 1
    return pathCount

def sumK(root, k):
    # Wrapper function to initiate prefixSum dictionary and start recursion
    if root is None:
        return 0
    
    prefixSum = {}
    return countPaths(root, k, 0, prefixSum)

# Example usage
nodes = [8, 4, 5, 3, 2, None, 2, 3, -2, None, 1, None, None]
root = buildTree(nodes)
printTree(root)
print('\n')
print(sumK(root, 7))