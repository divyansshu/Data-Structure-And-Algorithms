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
            print(curr_node.data, end=' ')
            curr_node = curr_node.next  
        print('\n')    

    def deleteAllOccurences(self):
        # Create a dummy node to simplify edge cases (e.g., deleting the head node)
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy  # Pointer to track the previous node
        
        # Traverse the linked list
        while self.head:
            # Check if the current node has duplicates
            if self.head.next and self.head.data == self.head.next.data:
                # Skip all nodes with the same value
                while self.head.next and self.head.data == self.head.next.data:
                    self.head = self.head.next
                # Link the previous node to the node after the duplicates
                prev.next = self.head.next
            else:
                # Move the previous pointer forward if no duplicates are found
                prev = prev.next
            # Move the head pointer forward
            self.head = self.head.next
        
        # Update the head of the linked list to the new list
        self.head = dummy.next
    
ll = LinkedList()
# Insert elements into the linked list
ll.insertAtEnd(1)                    
ll.insertAtEnd(2)                    
ll.insertAtEnd(3)                    
ll.insertAtEnd(3)                    
ll.insertAtEnd(4)                    
ll.insertAtEnd(4)                    
ll.insertAtEnd(5)

# Print the original linked list
ll.printLL()

print('list after deleting all repeated numbers')
# Delete all occurrences of duplicate elements
ll.deleteAllOccurences()
# Print the modified linked list
ll.printLL()                  