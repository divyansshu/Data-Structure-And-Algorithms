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
    
def topView(root):
    # Returns the top view of the binary tree as a list
    if root is None:
        return []
    
    q1 = deque()  # Queue for BFS: stores (node, horizontal distance)
    mp = {}       # Dictionary to store first node at each horizontal distance
    q1.append((root, 0))  # Start with root at horizontal distance 0
    
    while q1:
        node, hrz_d = q1.popleft()
        
        # If this horizontal distance is not seen before, add to map
        if hrz_d not in mp:
            mp[hrz_d] = node.data
            
        # Add left child with horizontal distance -1
        if node.left:
            q1.append((node.left, hrz_d-1))
        # Add right child with horizontal distance +1
        if node.right:
            q1.append((node.right, hrz_d+1))
    res = []
    # Collect results in order of horizontal distance (left to right)
    for key in sorted(mp):
        res.append(mp[key])
    return res

# Example usage
nodes = [10,20,30,40,60,90,100,None, None, None, None]
root = buildTree(nodes)
printTree(root)  # Print tree in preorder
print('\n')
print(topView(root))  # Print top view of the tree