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
            print(curr_node.data, end=",")
            curr_node = curr_node.next  
    
    def sizeOfLL(self):
        # Calculate and return the size of the linked list
        curr_node = self.head
        size = 0
        while curr_node:
            size += 1
            curr_node = curr_node.next
        return size    
    
    def deleteMiddle(self):
        # Delete the middle node of the linked list
        length = self.sizeOfLL()  # Get the size of the linked list
        
        if length == 1: 
            # If the list has only one node, set the head to None
            self.head = None
            return
        
        mid = length // 2  # Calculate the middle index
        
        count = 0
        curr = self.head
        prev = None
        while curr:
            if count == mid:
                # Stop when the middle node is reached
                break
            prev = curr  # Keep track of the previous node
            curr = curr.next  # Move to the next node
            count += 1
        
        # Skip the middle node by linking the previous node to the next node
        prev.next = curr.next
            
llist = LinkedList()

# Insert elements into the linked list
llist.insertAtEnd(1)        
llist.insertAtEnd(3)        
llist.insertAtEnd(4)        
llist.insertAtEnd(7)        
llist.insertAtEnd(1)        
llist.insertAtEnd(2)        
llist.insertAtEnd(6)        

# Print the linked list before deletion
llist.printLL()  

print('\nafter deleting middle node: ')

# Delete the middle node and print the linked list again
llist.deleteMiddle()
llist.printLL()   