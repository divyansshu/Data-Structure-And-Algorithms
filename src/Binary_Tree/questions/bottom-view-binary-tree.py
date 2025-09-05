class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

from collections import deque

def buildTree(nodes):
    # Builds a binary tree from a list of values (level order), where None means no node
    if not nodes or nodes[0] is None:
        return None
    
    root = Node(nodes[0])  # Create the root node
    q = deque([root])      # Queue for level order construction
    i = 1                  # Index for nodes list
    
    while q and i < len(nodes):
        node = q.popleft()
        
        # Assign left child if available
        if i < len(nodes) and nodes[i] is not None:
            node.left = Node(nodes[i])
            q.append(node.left)
        i += 1
        
        # Assign right child if available
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

def bottomView(root):
    # Returns the bottom view of the binary tree
    if root is None:
        return []
        
    q = deque()    # Queue for level order traversal
    mp = {}        # Map to store the last node at each horizontal distance
    q.append((root, 0))  # Start with root at horizontal distance 0
    while q:
        node, hd = q.popleft()
            
        mp[hd] = node.data  # Overwrite the value at hd, so the bottom-most node remains
            
        # Add left child with horizontal distance hd-1
        if node.left:
            q.append((node.left, hd-1))
        # Add right child with horizontal distance hd+1
        if node.right:
            q.append((node.right, hd+1))
        
    res = []
    # Extract the bottom view from the map, sorted by horizontal distance
    for key in sorted(mp):
        res.append(mp[key])
    return res

nodes = [10,20,30,40,60]
root = buildTree(nodes)
printTree(root)  # Print tree in preorder
print('\n')
print(bottomView(root))  # Print bottom view of the tree