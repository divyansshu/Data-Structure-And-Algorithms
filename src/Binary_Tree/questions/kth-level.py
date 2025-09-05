class Node:
    def __init__(self, data):
        # Initialize a new node with given data and left/right children as None
        self.data = data
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

def kthLevel(root, k):
    # Return a queue containing all nodes at the kth level of the tree
    if root is None:
        return None
    
    q = deque([root])  # Queue for level order traversal
    level = 1          # Current level
    flag = 0           # Flag to indicate kth level reached
    while q:
        size = len(q)  # Number of nodes at current level
        
        while size > 0:
            if level == k:
                flag = 1  # kth level reached
                break
            else:
                curr = q.popleft()
                # Add children to queue for next level
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            size -= 1
        
        if flag == 1:
            return q  # Return queue with kth level nodes
        level += 1

def printTree(root):
    # Print tree nodes in preorder traversal
    if root is None:
        return None
    print(root.data, end=' ')
    printTree(root.left)
    printTree(root.right)


if __name__ == '__main__':
    nodes = [1,2,3,4,5,6,7]  # Level order input for tree
    root = buildTree(nodes)   # Build tree
    printTree(root)           # Print tree in preorder
    print('\n')
    
    q = kthLevel(root, 3)     # Get nodes at 3rd level
    while q:
        curr = q.popleft()
        print(curr.data, end=' ')  # Print kth level nodes
