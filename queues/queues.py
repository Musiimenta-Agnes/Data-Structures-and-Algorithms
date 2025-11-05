from collections import deque # deque is used to remove items from both ends

## Create a queue and test queues
my_queue = deque()

#Add an elemennt to the queque
my_queue.append("eggs")
my_queue.append("oranges")
my_queue.append("mangoes")
my_queue.append("apples")

print("The queue consists of:", my_queue)


# Dequeue: This will remove the first element
removed = my_queue.popleft()
print("We have removed:", removed) #This will remove the first element


#  (Top element)
print("Front element:", my_queue[1]) # This will print the element that is on the top now



# Display the element in the third position
print("The third fruit is:", my_queue[2])  # This will print out apples because they are in the third position with index 2


# Check if the queue is empty
print("Is my_queue empty or not?", len(my_queue)==0)



# ) Double-Ended Queue (Deque)
# Insert and delete from both ends.

dq = deque()

dq.append(10)     # Add to rear
dq.append(20)      # Add to rear
dq.append(30)        # Add to rear
dq.appendleft(5)    # Add to front
dq.pop()            # Remove from rear
dq.popleft()        # Remove from front

print("My queue is:", dq)




#-----------------QUEUE CLASSES--------
# Queue Implementation Using Lists (Manual Way)


class Queue:  #Define a class named 'Queue' to represent our queue structure
    def __init__(self):  # This is the constructor; it runs when a new Queue object is created
        self.colors = []   # Initialize an empty list to hold the items in the queue

    

    def enqueue(self, item):  # Initialize an empty list to hold the items in the queue
            self.colors.append(item)  # Add the new item to the end (rear) of the list



    def dequeue(self):  # Define a method to remove an item from the front of the queue
         if not self.is_empty():  # Check if the queue is not empty before removing
              return self.colors.pop(0)   # Remove and return the first item (index 0) — FIFO principle
         return "The queue is empty"   # If the queue is empty, return a message instead of removing
    


    def front(self):   # Define a method to look at the front item without removing it
         if not self.is_empty(): # Check if the queue is not empty
              return self.colors[0]  # Return the first item in the list (front of the queue)
         return "The queue is empty"  # If there’s nothing in the queue, return this message

    
    

    def is_empty(self):  # Define a method to check whether the queue is empty
         return len(self.colors)==0   # Returns True if queue has no items, False otherwise
    
    def display(self):  # Define a method to show the current contents of the queue
         print("My queue consists of:", self.colors)   # Print the queue list so you can see its elements
           
    



# assume the Queue class is defined above

# 1) Create a new queue object
q = Queue()               # q.queue == []

# 2) Enqueue (add) items to the queue
q.enqueue(10)             # q.queue -> [10]
q.enqueue(20)             # q.queue -> [10, 20]
q.enqueue(30)             # q.queue -> [10, 20, 30]

# 3) Display the queue contents
q.display()               # prints: Queue: [10, 20, 30]

# 4) Peek at the front item without removing it
print("Front:", q.front())   # prints: Front: 10

# 5) Dequeue (remove) the front item
print("Dequeued:", q.dequeue())  # removes 10, prints: Dequeued: 10
q.display()                       # prints: Queue: [20, 30]

# 6) Dequeue remaining items
print("Dequeued:", q.dequeue())  # removes 20, prints: Dequeued: 20
print("Dequeued:", q.dequeue())  # removes 30, prints: Dequeued: 30

# 7) Now the queue is empty — check and try unsafe ops
print("Is empty?", q.is_empty())     # prints: Is empty? True
print("Dequeue on empty:", q.dequeue())  # prints: Dequeue on empty: Queue is empty
print("Front on empty:", q.front())       # prints: Front on empty: Queue is empty

