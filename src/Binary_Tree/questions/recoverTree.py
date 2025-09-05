class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
    
def buildBST(root,val):
    if root is None:
        return Node(val)
    
    if val < root.val:
        root.left = buildBST(root.left, val)
    else:
        root.right = buildBST(root.right, val)
    return root

def BST(nodes):
    root = None    for val in nodes:
        root = buildBST(root, val)
    return root

def printTree(root):
    if root is None:
        return None
    printTree(root.left)
    print(root.val, end=' ')
    printTree(root.right)
    
    
def recoverTree(A):
    res = []
 

nodes = [2,3,1]
root = BST(nodes)
printTree(root)
print('\n')
print(recoverTree(root))
