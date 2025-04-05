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
            print(curr_node.data, end=" ")
            curr_node = curr_node.next 
        print("\n")     
    
    def rotateRight(self, k):
        # Rotate the linked list to the right by k positions
        
        # If the list is empty or has only one node, no rotation is needed
        if self.head is None:
            return self.head

        # Calculate the length of the linked list and get the tail node
        length, tail = 1, self.head
        while tail.next:
            tail = tail.next
            length += 1

        # Reduce k to within the bounds of the list length
        k = k % length
        if k == 0: 
            # If k is 0 after modulo operation, no rotation is needed
            return
        
        # Find the new head of the rotated list
        curr = self.head
        for i in range(length - k - 1):
            curr = curr.next
        
        # Update the pointers to rotate the list
        newHead = curr.next    # The new head is the next node after the current node
        curr.next = None       # Break the link to form the new end of the list
        tail.next = self.head  # Connect the old tail to the old head
        self.head = newHead    # Update the head to the new head

# Create a linked list and insert elements
ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)

# Print the original linked list
ll.printLL()

# Rotate the linked list to the right by 10 positions
ll.rotateRight(10)

# Print the rotated linked list
ll.printLL()