class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

from collections import deque

def buildTree(nodes):
    # Builds a binary tree from a list of values (level order), where None means no node
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
        
def isLeaf(root):
    # Checks if a node is a leaf (no children)
    if root.left is None and root.right is None:
        return True
    return False
        
def collectLeftBoundary(root, res):
    # Collects the left boundary (excluding leaves)
    if root is None or isLeaf(root):
        return
        
    res.append(root.data)
    if root.left:
        collectLeftBoundary(root.left, res)
    elif root.right:
        collectLeftBoundary(root.right, res)
    
def collectLeaves(root, res):
    # Collects all leaf nodes in the tree
    if root is None:
        return 
    if isLeaf(root):
        res.append(root.data)
        return
        
    collectLeaves(root.left, res)
    collectLeaves(root.right, res)
    
def collectRightBoundary(root, res):
    # Collects the right boundary (excluding leaves), in bottom-up order
    if root is None or isLeaf(root):
        return
        
    if root.right:
        collectRightBoundary(root.right, res)
    elif root.left:
        collectRightBoundary(root.left, res)
    res.append(root.data)  # Add after child visit for bottom-up order
        
def boundaryTraversal(root):
    # Returns the boundary traversal of the binary tree
    res = []
    if not root:
        return res
        
    if not isLeaf(root):
        res.append(root.data)  # Add root if it's not a leaf
        
    collectLeftBoundary(root.left, res)   # Left boundary
    collectLeaves(root, res)              # All leaves
    collectRightBoundary(root.right, res) # Right boundary
    return res

# Example usage
nodes = [1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None]
root = buildTree(nodes)
printTree(root)
print('\n')
print(boundaryTraversal(root))