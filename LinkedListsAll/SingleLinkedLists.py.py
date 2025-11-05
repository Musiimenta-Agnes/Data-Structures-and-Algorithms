# Linked Lists in Python

class Node:
    # initalize the data
    def __init__(self, data):
        # stores the vlaue of the node
        self.data = data   
        # points the next node
        self.next = None
        
    # initialize the full list
class LinkedList:
    def __init__(self):
        # the first node in the list, when empty it head is None
            self.head = None
             

             
    # insert at the beginning
    def insertAtBegin(self, data):
        # create a new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            # link it to the current head
            new_node.next = self.head
            # make it the new head
            self.head = new_node
    



    # insert at an index
    def insertAtIndex(self, data, index):
        # insert at beginning
        if index == 0:
            self.insertAtBegin(data)
            return

        new_node = Node(data)
        current = self.head
        position = 0

        # Traverse to node just before the index
        while current is not None and position < index - 1:
            current = current.next
            position += 1

        if current is None:
            print("Index not present")
        else:
            # previous node points to the new node
            new_node.next = current.next
            current.next = new_node     
    





    # insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        # if the list is empty
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        # Traverse to the last node
        while current.next:
            current = current.next

        # add new node at the end
        current.next = new_node
        








    # update node of a linked list
    # at a given position
    def updateNode(self, val, index):
        current_node = self.head   
        position = 0

        # Traverse until the given index, but start from the first node
        while current_node is not None and position < index:
            current_node = current_node.next
            position += 1

        # Check if we found the node
        if current_node is not None:
            current_node.data = val
            print(f"Node at index {index} updated to {val}")
        else:
            print("Index not present")
            








    # delete a node
    # remove first node
    def removeFirstNode(self):
        if(self.head == None):
            return 
        self.head = self.head.next
        
    # remove last node
    def removeLastNode(self):
        if self.head is None:
            return
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
            
        current_node.next = None
        



        
    # remove at an index
    def removeAtIndex(self, index):
        # If the list is empty, do nothing
        if self.head is None:
            print("List is empty")
            return
        
        # If the node to remove is the first one
        if index == 0:
            self.head = self.head.next
            return
        
        # Start from the head node
        current_node = self.head
        position = 0

        # Traverse to the node just before the one we want to delete
        while current_node is not None and position < index - 1:
            current_node = current_node.next
            position += 1

        # If we reached the end before finding the index
        if current_node is None or current_node.next is None:
            print("Index not present")
            return

        # Skip over the node to delete it
        current_node.next = current_node.next.next
        






    # get length of linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head

        # Traverse the linked list
        while current_node:
            size += 1
            current_node = current_node.next

        return size









    # Print the linked list
    def printList(self):
        current = self.head
        # move to the next node until the end ir None
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        

ll = LinkedList()
ll.insertAtBegin(10)
ll.insertAtBegin(20)
ll.insertAtEnd(30)
ll.insertAtIndex(15, 1)
ll.insertAtIndex(5, 0)
ll.insertAtIndex(50, 10)
ll.updateNode(100,1)
ll.removeFirstNode()
ll.removeLastNode()
ll.removeAtIndex(1)
print(ll.sizeOfLL())
ll.printList()
            