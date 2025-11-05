class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Points to itself
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def insertAtBeginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        prev = None

        # If head node is to be deleted
        if current.data == key:
            # Find last node
            while current.next != self.head:
                current = current.next
            if self.head == self.head.next:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return

        # Traverse and find the node
        current = self.head
        while current.next != self.head and current.next.data != key:
            current = current.next

        if current.next.data == key:
            current.next = current.next.next
        else:
            print("Node not found")

    def printList(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

cll = CircularLinkedList()
cll.insertAtEnd(10)
cll.insertAtEnd(20)
cll.insertAtEnd(30)
cll.insertAtBeginning(5)
cll.deleteNode(20)
cll.printList()