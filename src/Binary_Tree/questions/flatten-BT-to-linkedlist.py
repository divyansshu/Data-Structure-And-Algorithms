class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

from collections import deque    

def buildTree(nodes):
    # Builds a binary tree from a list of values (level order)
    if not nodes or nodes[0] is None:
        return None
    
    index = 1
    root = Node(nodes[0])
    q = deque([root])
    
    while index < len(nodes) and q:
        node = q.popleft()
        # Assign left child
        if index < len(nodes) and nodes[index]:
            node.left = Node(nodes[index])
            q.append(node.left)
        index += 1
        
        # Assign right child
        if index < len(nodes) and nodes[index]:
            node.right = Node(nodes[index])
            q.append(node.right)
        index += 1
    return root

def preorder(root):
    # Prints preorder traversal of the tree
    if root is None:
        return None
    
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

nextRight = None

def flatten(root):
    # Flattens the binary tree to a linked list in-place (right pointers only)
    global nextRight
    if root is None:
        return 
    
    # Recursively flatten right subtree first
    flatten(root.right)
    # Then flatten left subtree
    flatten(root.left)
    
    # Set left to None and right to previously visited node
    root.left = None
    root.right = nextRight
    # Update nextRight to current node
    nextRight = root


nodes = [1,2,5,3,4,None,6]
root = buildTree(nodes)
preorder(root)  # Print original preorder traversal
print('\n')
flatten(root)   # Flatten the tree
preorder(root)  # Print preorder traversal of flattened tree