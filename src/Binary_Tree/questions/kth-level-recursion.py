class Node:
    def __init__(self, val):
        # Initialize a binary tree node with given value
        self.data = val
        self.left = self.right = None

from collections import deque

def buildTree(nodes):
    # Build a binary tree from a list of node values (level order)
    if not nodes and nodes[0] is None:
        return None
    
    root = Node(nodes[0])  # Create root node
    q = deque([root])      # Queue for level order construction
    idx = 1                # Index for traversing nodes list
    
    while q and idx < len(nodes):
        curr = q.popleft()
        # Add left child if present
        if idx < len(nodes) and nodes[idx]:
            curr.left = Node(nodes[idx])
            q.append(curr.left)
        idx += 1
        
        # Add right child if present
        if idx < len(nodes) and nodes[idx]:
            curr.right = Node(nodes[idx])
            q.append(curr.right)
        idx += 1
    return root

def preorder(root):
    # Preorder traversal: root -> left -> right
    if root is None:
        return None
    
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def kthLevel(root, k):
    # Find all nodes at the kth level using recursion
    def backtrack(root, level ,res):
        if root is None:
            return None
        
        # If current level matches k, add node's data to result
        if level == k:
            res.append(root.data)
            return
        
        # Recurse for left and right children, incrementing level
        backtrack(root.left, level+1, res)
        backtrack(root.right, level+1, res)
    
    res = []
    backtrack(root, 1, res)  # Start from level 1 (root)
    return res

# Example usage
nodes = [1,2,3,4,5,6,7]
root = buildTree(nodes)

preorder(root)  # Print preorder traversal
print('\n')

print(kthLevel(root, 3))  # Print all nodes at level 3