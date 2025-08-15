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
        # Assign left child if available
        if idx < len(nodes) and nodes[idx]:
            node.left = Node(nodes[idx])
            q.append(node.left)
        idx += 1
        # Assign right child if available
        if idx < len(nodes) and nodes[idx]:
            node.right = Node(nodes[idx])
            q.append(node.right)
        idx += 1
    return root

def findIP(curr):
    # Find the inorder predecessor (rightmost node in left subtree)
    IP = curr.left
    while IP.right and IP.right != curr:
        IP = IP.right
    return IP

def morris_inorder(root):
    # Morris Inorder Traversal without recursion or stack
    curr = root
    while curr:
        if curr.left is None:
            # If no left child, print current node and move right
            print(curr.data, end=' ')
            curr = curr.right
        else:
            # Find inorder predecessor
            IP = findIP(curr)
            if IP.right is None:
                # Make current node as right child of its inorder predecessor
                IP.right = curr
                curr = curr.left
            else:
                # Revert the changes (fix the right child of predecessor)
                IP.right = None
                print(curr.data, end=' ')
                curr = curr.right
                
nodes = [1,2,3,6,7,4,5]
root = buildTree(nodes)
morris_inorder(root)
