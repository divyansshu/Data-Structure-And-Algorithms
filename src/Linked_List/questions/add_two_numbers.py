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
    
    def sizeOfLL(self):
        # Calculate and return the size of the linked list
        curr_node = self.head
        size = 0
        while curr_node:
            size += 1
            curr_node = curr_node.next  
        return size   
    
    def addTwoNumbers(self, l1, l2):
        # Add two numbers represented by two linked lists
        temp1 = l1.head  # Pointer to traverse the first linked list
        temp2 = l2.head  # Pointer to traverse the second linked list
        carry = 0        # Variable to store carry from the addition
        l3 = LinkedList()  # Resultant linked list to store the sum
        
        # Loop until both lists are fully traversed and no carry remains
        while temp1 or temp2 or carry:
            # Get the current digit from the first list, or 0 if the list is exhausted
            digit1 = temp1.data if temp1 else 0
            # Get the current digit from the second list, or 0 if the list is exhausted
            digit2 = temp2.data if temp2 else 0
            
            # Calculate the sum of the digits and the carry
            sum = digit1 + digit2 + carry
            # Insert the last digit of the sum into the resultant linked list
            l3.insertAtEnd(sum % 10)
            # Update the carry for the next iteration
            carry = sum // 10
            
            # Move to the next node in the first list, if available
            if temp1: temp1 = temp1.next
            # Move to the next node in the second list, if available
            if temp2: temp2 = temp2.next
        
        # Return the resultant linked list
        return l3      
            
# Create the first linked list and insert digits of the first number
l1 = LinkedList()
l1.insertAtEnd(2)
l1.insertAtEnd(4)
l1.insertAtEnd(3)

# Print the first linked list
l1.printLL()

# Create the second linked list and insert digits of the second number
l2 = LinkedList()
l2.insertAtEnd(5)
l2.insertAtEnd(6)
l2.insertAtEnd(4)

# Print the second linked list
l2.printLL()

# Add the two numbers represented by the linked lists
result = l1.addTwoNumbers(l1, l2)

# Print the resultant linked list
result.printLL()