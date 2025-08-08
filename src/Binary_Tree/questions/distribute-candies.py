class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

from collections import deque    

def buildTree(nodes):
    # If the first node is -1, the tree does not exist
    if nodes[0] == -1:
        return 'Tree does not exist'
    
    root = Node(nodes[0])
    q = deque([root])
    index = 1
    # Build the tree using level order traversal
    while q and index < len(nodes):
        node = q.popleft()
        
        # Assign left child if not -1
        if index < len(nodes) and nodes[index] != -1:
            node.left = Node(nodes[index])
            q.append(node.left)
        index += 1
        
        # Assign right child if not -1
        if index < len(nodes) and nodes[index] != -1:
            node.right = Node(nodes[index])
            q.append(node.right)
        index += 1
    return root

def printTree(root):
    # Preorder traversal to print the tree
    if root is None:
        return None
    print(root.data, end=' ')
    printTree(root.left)
    printTree(root.right)
    
def distributeCandies(root):
    # This function returns the minimum number of moves required
    # to distribute candies so every node has exactly one candy.
    steps = 0
    def dfs(root):
        nonlocal steps
        # Base case: if node is None, return 0
        if root is None:
            return 0
        
        # Recursively compute for left and right subtrees
        left = dfs(root.left)
        right = dfs(root.right)
        # Add the absolute values of left and right to steps
        steps += abs(left) + abs(right)
        # Return the excess candies at this node
        return (root.data - 1) + left + right
    dfs(root)
    return steps
    
    
# Read input, build tree, print tree, and print result
nodes = list(map(int, input().strip().split()))
root = buildTree(nodes)
printTree(root)
print('\n')
print(distributeCandies(root))
