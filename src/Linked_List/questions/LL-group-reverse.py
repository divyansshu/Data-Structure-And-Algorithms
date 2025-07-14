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
    
    def reverseKGroup(self, k):
        st = []  # Stack to hold nodes for reversal
        temp = self.head
        prev = None  # Tracks the last node of the previous reversed group
        while temp is not None:
            K = k  # Counter for group size
            # Push up to k nodes onto the stack
            while K > 0 and temp is not None:
                st.append(temp)
                temp = temp.next
                K -= 1
            # Pop nodes from stack to reverse the group
            while st:
                if prev is None:
                    prev = st.pop()  # First node of reversed group becomes new head
                    self.head = prev
                else:
                    prev.next = st.pop()  # Connect previous group to current reversed node
                    prev = prev.next
        # Set the next of last node to None to terminate the list
        prev.next = None

ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(2)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
ll.insertAtEnd(6)
ll.insertAtEnd(7)
ll.insertAtEnd(8)

ll.printLL()  # Print original list

ll.reverseKGroup(4)  # Reverse nodes in groups of 4
ll.printLL()  # Print modified list