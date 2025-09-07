class Node:
    def __init__(self, val):
        self.data = val  # Store the value of the node
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list
    
    def insert(self, data):
        # Create a new node with the given data
        node = Node(data)
        if self.head is None:
            # If the list is empty, set the new node as head
            self.head = node
            return

        # Otherwise, traverse to the end and insert the new node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
    
    def printLL(self):
        # Print all elements in the linked list
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
    
    def getKthFromLast(self, k):
        # Return the kth node from the end of the list
        if self.head is None:
            return -1  # If list is empty, return -1
        
        slow = fast = self.head
        # Move fast pointer k steps ahead
        for _ in range(k):
            if not fast:
                return -1  # If k is greater than the length of the list
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        # Now, slow is at the kth node from the end
        return slow.data
                 

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)
ll.insert(9)

ll.printLL()  # Print the linked list
k = 2
print(f'{k}th Node from End of Linked List: ', ll.getKthFromLast(2))  # Print kth node from end