class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.next = None        

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with no head
        self.head = None
        
    def insertAtEnd(self, data):
        # Insert a new node with the given data at the end of the linked list
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        # Traverse to the end of the list
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        # Link the last node to the new node
        curr_node.next = new_node
        
    def printLL(self):
        # Print all elements of the linked list
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next  
    
    def sizeOfLL(self):
        # Calculate and return the size of the linked list
        curr_node = self.head
        size = 0
        while curr_node:
            size += 1
            curr_node = curr_node.next
        return size    
                              
    def removeNthFromEnd(self, n):
        # Remove the nth node from the end of the linked list
        length = self.sizeOfLL()  # Get the size of the linked list
        
        if length == 1:
            # If the list has only one node, remove it by setting head to None
            self.head = None
            return
            
        targetNode = length - n  # Calculate the position of the target node from the start
        
        if targetNode == 0:
            # If the target node is the head, update the head to the next node
            self.head = self.head.next
            return
        
        # Traverse to the target node
        count = 0
        prev = None
        curr = self.head
        while count < targetNode:
            prev = curr
            curr = curr.next
            count += 1
        # Remove the target node by updating the previous node's next pointer
        prev.next = curr.next        
            
        
llist = LinkedList()

# Insert elements into the linked list
llist.insertAtEnd(1)        
llist.insertAtEnd(2)        
llist.insertAtEnd(3)        
llist.insertAtEnd(4)        
llist.insertAtEnd(5)

# Print the linked list before deletion
llist.printLL()

# Remove the 3rd node from the end of the list
llist.removeNthFromEnd(3)

print('after deleting nth node from last')

# Print the linked list after deletion
llist.printLL()