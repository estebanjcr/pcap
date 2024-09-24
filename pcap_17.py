# Instance Variables

class ExampleClass:
    def __init__(self, val=1):   # set default value for <first> variable
    	self.first = val
    
    def set_second(self, val):
    	self.second = val


example_object_1 = ExampleClass()

example_object_2 = ExampleClass(2)
example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5   # added property 'on the fly'


# __dict__ predefined object property

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


# mangling an instance's private variable

class PrivExampleClass(ExampleClass):
    def __init__(self):
    	ExampleClass.__init__(self)
    	self.__fourth = 6

example_object_4 = PrivExampleClass()
print(example_object_4.__dict__)
