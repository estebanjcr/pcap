# Checking an attribute's existence

class ExampleClass:
    def __init__(self, val):
    	if val % 2 == 0:
    		self.a = 1
    	else:
    		self.b = 1

example_object = ExampleClass(1)
#print(example_object_1.a)   # AttributeError
print(example_object.b)


# catching the error with a try-except block

try:
    print(example_object.b)
    print(example_object.a)
except AttributeError:
    pass


# hasattr function

if hasattr(example_object, "b"):
    print(example_object.b)
elif hasattr(example_object, "a"):
    print(example_object.a)


# hasattr fuction in a class

class ExampleClass2:
    a = 1
    def __init__(self):
    	self.b = 2

example_object_2 = ExampleClass2()
print(hasattr(example_object_2, 'b'))
print(hasattr(example_object_2, 'a'))
print(hasattr(ExampleClass2, 'b'))
print(hasattr(ExampleClass2, 'a'))