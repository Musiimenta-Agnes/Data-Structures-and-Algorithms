
# Create a node called MyList

class Node:
    def __init__(self, data):
        self.data = data # This stores the data (value)
        self.next = None # This creates a value with  pointer to the next one. It is none by defult



 # Initialise th full list
class MySngleList:
    def __init__(self):
        self.head = None # The first node in the list when empty, the head is none




# Insert a new node at the beginning
    def insertAtBegin(self, data):
        # Create a new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            #Link it to the current head
            new_node.next = self.head
            #Then make it the new head
            self.head = new_node



        # Print the Linked List
    def PrintList(self):
            current = self.head

            # Move to the next node unti the next is None
            while current: # Keep looping until we reach the end of the list.
                 print(current.data, end=" ->") # Print the data of the current node, followed by " ->" instead of moving to a new line.
                 current = current.next
            print("None")


 # Create the nodes
values = MySngleList()
values.insertAtBegin(1)
values.insertAtBegin(2)






