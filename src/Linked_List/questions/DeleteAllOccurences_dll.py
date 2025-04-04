class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, val):
        
        newNode = Node(val)
        
        #case 1: if head is None
        if self.head is None:
            self.head = newNode
            return
        
        # case 2: if head is not None   
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
    
    def printDLL(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('\n')
    
    def deleteAllOccurence(self, key):
        temp = self.head
        while temp:
            # case 1: if head is equal to key
            if key == self.head.data:
                self.head = temp.next
                
            # case 2: if last node is key
            elif temp.data == key and temp.next is None:
                (temp.prev).next = None
                
            # case 3: if other nodes are key     
            elif temp.data == key:
                (temp.prev).next = temp.next
                (temp.next).prev = temp.prev
                 
            temp = temp.next   
    
dll = LinkedList()
dll.insertAtEnd(2)            
dll.insertAtEnd(2)            
dll.insertAtEnd(10)            
dll.insertAtEnd(8)            
dll.insertAtEnd(4)
dll.insertAtEnd(2)
dll.insertAtEnd(5)
dll.insertAtEnd(2)
dll.printDLL()  

dll.deleteAllOccurence(2)
dll.printDLL()          
                
             
            
            
        
                    
        