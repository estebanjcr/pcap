# Stack data structure
# LIFO: Last-In First-Out

class Stack:
    def __init__(self):   # constructor function/method
    	print("Hi")   # ran at instantiation
    	self.stack_list_1 = []   # public variable
    	self.__stack_list_2 = []   # private variable
    
    def push(self, val):
    	self.stack_list_1.append(val)
    
    def pop(self):
    	val = self.stack_list_1[-1]
    	del self.stack_list_1[-1]
    	return val

stack_object_1 = Stack()   # instantiation
for i in range(0, 6):
    stack_object_1.push(i)
stack_object_1.pop()
print(stack_object_1.stack_list_1)


# Subclass & Superclass

class AddingStack(Stack):
    def __init__(self):
    	Stack.__init__(self)
    	self.__sum = 0
    
    def get_sum(self):
    	return self.__sum
    
    def push(self, val):    # method override
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
    	val = Stack.pop(self)
    	self.__sum -= val
    	return val

stack_object_2 = AddingStack()
for i in range(0, 6):
    stack_object_2.push(i)
stack_object_2.pop()
stack_object_2.pop()
print(stack_object_2.stack_list_1)
print(stack_object_2.get_sum())
