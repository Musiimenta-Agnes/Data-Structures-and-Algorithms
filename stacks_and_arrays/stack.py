class Colors: # This creates a class called Colors
    def __init__(self): # This initializes
        self.colors = []
    

    # We define the push method to add a color to the stack
    def push(self, color):
        self.colors.append(color)
    

    # We define the pop method to remove and return the last color added to the stack
    #We shall first check whether the stack is empty before popping an element
    def pop(self):
        if self.isEmpty():
            return "Colors is empty"
        return self.colors.pop()
    
    #  We define the isEmpty method to check if the stack is empty
    # It returns True if the stack is empty, otherwise False
    
    def isEmpty(self):
        return len(self.colors) == 0
    

    # we need to get the size of the stack
    def size(self):
        return len(self.colors)




# Using the Colors stack class
myColors = Colors()

myColors.push('Yellow')
myColors.push('Blue')
myColors.push('Orange')
print("colors: ", myColors.colors)

print("Pop: ", myColors.pop())

print("isEmpty: ", myColors.isEmpty())

print("Size: ", myColors.size())