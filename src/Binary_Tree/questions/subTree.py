class Node:
    # Node class to represent each node in the binary tree
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

from collections import deque

def buildTree(nodes):
    # Builds a binary tree from a list of node values (level order)
    if not nodes and nodes[0] is None:
        return None

    root = Node(nodes[0])  # Create root node
    q = deque([root])      # Queue for level order traversal
    idx = 1

    while q and idx < len(nodes):
        curr = q.popleft()
        # Assign left child if value exists
        if idx < len(nodes) and nodes[idx]:
            curr.left = Node(nodes[idx])
            q.append(curr.left)
        idx += 1

        # Assign right child if value exists
        if idx < len(nodes) and nodes[idx]:
            curr.right = Node(nodes[idx])
            q.append(curr.right)
        idx += 1
    return root

def preorder(root):
    # Preorder traversal (root, left, right)
    if root is None:
        return None

    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def isIdentical(node, subroot):
    # Checks if two trees are identical
    if node is None and subroot is None:
        return True
    if node is None or subroot is None or node.data != subroot.data:
        return False

    # Recursively check left and right subtrees
    return isIdentical(node.left, subroot.left) and isIdentical(node.right, subroot.right)

def subTree(root, subroot):
    # Checks if subroot is a subtree of root
    if root is None:
        return False

    # If current node matches subroot, check for identical trees
    if root.data == subroot.data:
        if isIdentical(root, subroot):
            return True

    # Recursively check left and right subtrees
    return subTree(root.left, subroot) or subTree(root.right, subroot)

# Example usage
tree1 = [1,2,3,4,5,None, 6]
root = buildTree(tree1)
print('Main Tree')
preorder(root)
print('\n')

tree2 = [2,4,5]
subroot = buildTree(tree2)
print('sub Tree')
preorder(subroot)
print('\n')

print('is tree2 sub tree of tree1: ')
print(subTree(root, subroot))
