class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Link new node to old head
        if self.head is not None:
            self.head.prev = new_node  # Old head's prev = new node
        self.head = new_node  # New node becomes the new head

    def insertAtEnd(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next

        # Adjust pointers
        current.next = new_node
        new_node.prev = current

    def deleteNode(self, data):
        current = self.head

        # Empty list
        if current is None:
            print("List is empty")
            return

        # If the node to delete is the head
        if current.data == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        # Search for node to delete
        while current and current.data != data:
            current = current.next

        # Node not found
        if current is None:
            print("Node not found")
            return

        # Adjust links
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
            
    def printForward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def printBackward(self):
        current = self.head
        # Go to the last node first
        while current and current.next:
            current = current.next

        # Traverse backward
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Test the list
dll = DoublyLinkedList()
dll.insertAtBeginning(10)
dll.insertAtBeginning(20)
dll.insertAtEnd(30)
dll.insertAtEnd(40)
dll.deleteNode(10)

print("Forward traversal:")
dll.printForward()

print("Backward traversal:")
dll.printBackward()
