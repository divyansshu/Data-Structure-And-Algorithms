class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode  # If list is empty, set new node as head
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next  # Traverse to the end of the list
        temp.next = newNode  # Insert new node at the end

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')  # Print current node's data
            temp = temp.next  # Move to next node
        print('\n')

    def rotateLeft(self, k):
        # If list is empty or has only one node or k is 0, do nothing
        if self.head.next is None or k == 0:
            return self.head

        # Find the length of the linked list
        temp = self.head
        length = 1
        while temp.next is not None:
            temp = temp.next
            length += 1

        # Adjust k if it's greater than length
        k %= length
        if k == 0:
            return self.head

        # Connect the last node to the head to make it circular
        temp.next = self.head

        # Traverse to the (k)th node
        temp = self.head
        for _ in range(1, k):
            temp = temp.next

        # Set the new head and break the loop
        self.head = temp.next
        temp.next = None

ll = LinkedList()
ll.insertAtEnd(10)
ll.insertAtEnd(20)
ll.insertAtEnd(30)
ll.insertAtEnd(40)
ll.insertAtEnd(50)

# Print the original linked list
ll.printLL()

# Rotate the linked list to the left by 4 positions
ll.rotateLeft(4)

# Print the rotated linked list
ll.printLL()