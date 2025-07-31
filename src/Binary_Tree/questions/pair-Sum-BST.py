class Node:
    def __init__(self, val):
        self.data = val
        self.left = self.right = None

# Function to insert a value into the BST
def buildBST(root, val):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = buildBST(root.left, val)
    else:
        root.right = buildBST(root.right, val)
    return root

# Function to build a BST from a list of values
def BST(nodes):
    root = None
    for val in nodes:
        if val is not None:
            root = buildBST(root, val)
    return root

# Preorder traversal (root, left, right)
def preorder(root):
    if root is None:
        return None
    
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

# Function to check if there exists a pair with given sum in BST
def pairSum(root, target):
    st = set()  # Set to store visited node values

    # Helper function for DFS traversal
    def dfs(root):
        if root is None:
            return False
        
        # Check if complement exists in set
        if target - root.data in st:
            return True
        
        # Add current node value to set
        st.add(root.data)
        # Continue search in left and right subtrees
        return dfs(root.left) or dfs(root.right)
    return dfs(root)
    
# Example usage
nodes = [7,3,8, 2, 4, None, 9]
root = BST(nodes)
preorder(root)
print('\n')

print(pairSum(root, 12))
