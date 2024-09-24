# Class variables

class ExampleClass:
    counter = 0
    def __init__(self, val=1):
        self.first = val
        ExampleClass.counter += 1

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(3)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)


# mangling a class' private variable

class PrivExampleClass:
    __counter = 0
    def __init__(self, val=1):
        self.first = val
        PrivExampleClass.__counter += 1

example_object_4 = PrivExampleClass(4)
print(example_object_4.__dict__, example_object_4._PrivExampleClass__counter)


# __dict__ class property

class ExampleClass3:
    varia = 1
    def __init__(self, val):
    	ExampleClass3.varia = val

print(ExampleClass3.__dict__, "\n")

example_object_5 = ExampleClass3(5)
print(ExampleClass3.__dict__, "\n")

print(example_object_5.__dict__)