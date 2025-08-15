class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

from collections import deque        

def buildTree(nodes):
    # Build a binary tree from a list of values (level order)
    if not nodes or nodes[0] is None:
        return None
    idx = 1
    root = Node(nodes[0])
    q = deque([root])
    
    while q and idx < len(nodes):
        node = q.popleft()
        # Assign left child
        if idx < len(nodes) and nodes[idx]:
            node.left = Node(nodes[idx])
            q.append(node.left)
        idx += 1
        # Assign right child
        if idx < len(nodes) and nodes[idx]:
            node.right = Node(nodes[idx])
            q.append(node.right)
        idx += 1
    return root

def preorder(root):
    # Preorder traversal: root -> left -> right
    if root is None:
        return None
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

def widthOfBinaryTree(root):
    # Calculate the maximum width of the binary tree
    q = deque()
    q.append((root, 0))  # Each element is (node, index)
    maxwidth = 0
    while q:
        currLevelSize = len(q)
        st = q[0][1]      # Index of first node at current level
        end = q[-1][1]    # Index of last node at current level
        maxwidth = max(maxwidth, (end - st) + 1)

        for i in range(currLevelSize):
            node, idx = q.popleft()
            # Assign indices to children as in a complete binary tree
            if node.left:
                q.append((node.left, 2 * idx + 1))
            if node.right:
                q.append((node.right, 2 * idx + 2))
    return maxwidth

# Example usage:
# nodes = [1,3,2,5,3,None,9]
nodes = [1,3,2,5,None,None,9,6,None,7,None]
root = buildTree(nodes)
preorder(root)  # Print preorder traversal
print('\n')

print(widthOfBinaryTree(root))  # Print maximum width of the tree
