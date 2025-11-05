# creating a class Node with 2 variables data and next
class Node: 
  def __init__(self, data): # constructor
    self.data = data
    self.next = None  
    # Here, the linked list is having only one node so we are not linking tp another 
    # node therefore next value is none/null

# creating a singleLinkedList class for linking to another node
class SingleLinkedList: 
    def __init__(self):
       self.head = None # initially there are no elements so head = none. The head is the first element of a linked list
       
    # function for displaying data   
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head # temporary variable for storing head
            while temp:
                print(temp.data, "-->", end="") # printing the data of each node
                temp = temp.next # it will keep moving to the next

# in a single linked list, the address of the next of the last node is null or none but 
# for circularr linked lists, the address of the nxt in the last node is the address of the first one

# CREATING A CIRCULAR LINKED LIST            
class CircularLinkedList:
    def __init__(self): # intialzing head and tail. Head is the first node and tail is the last node
        self.head = None # head is pointing to nothing because initially we have an empty circular linked list
        self.tail = None
    
    # function for displaying the circular linked list
    def display(self):
        # we have to display data starting from head to tail
        if self.head is None: # wen we have an empty list
            print("Empty list") 
        else:
            temp = self.head # temporary variable for storing head
            print(temp.data, "-->", end="") # printing the data of each node
            while temp.next != self.head: # this when the node does not have the address of the first node
                temp = temp.next
                print(temp.data, "-->", end="") 
            
             
     
     
    # function for displaying the circular linked list
    
    
       
# creating an object to be used to add the node
L= SingleLinkedList() # created an empty linked list
n1 = Node(10) # created a node. with data 10 and next none

# assigned head to n1
L.head =n1

n2 = Node(20) # creating another node
L.head.next =n2
n3 = Node(30) # creating another node
n2.next = n3 # assigning n2 next 
L.display()

CLL = CircularLinkedList() # empty circular linked list
CLL.display()
node_1 = Node(2)
CLL.head = node_1
CLL.tail = node_1
CLL.tail.next = CLL.head
node_2 = Node(3)
CLL.tail.next = node_2
CLL.tail = node_2
CLL.tail.next = CLL.head  # closing the circle
CLL.display()