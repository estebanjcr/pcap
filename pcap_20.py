# Methods in detail

class Classy:
    def method(self, par):
    	print("method: ", par)

obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)


# self parameter to access the object's instance and class variables

class Classy:
    varia = 2
    def method(self):
    	print("varia:", self.varia, "var:", self.var)

obj = Classy()
obj.var = 2
obj.method()


# self parameter to invoke other object/class methods from inside the class

class Classy:
     def other(self):
     	print("other")
     
     def method(self):
     	print("method")
     	self.other()

obj = Classy()
obj.method()


# __init__ method (constructor)

class Classy:
    def __init__(self, value):
        self.var = value

obj = Classy("object")
print(obj.var)

class Classy:
    def __init__(self, value=None):
    	self.var = value

obj1 = Classy("object")
obj2 = Classy()

print(obj1.var)
print(obj2.var)

class Classy:
    def visible(self):
    	print("visible")
    
    def __hidden(self):
    	print("hidden")

obj = Classy()
obj.visible()

try:
    obj.hidden()
except:
    print("failed")

obj._Classy__hidden()


# predefined methods and attributes

class SuperOne:
    pass

class SuperTwo:
    pass

class Classy(SuperOne, SuperTwo):
    varia = 1
    def __init__(self):
    	self.var = 2
    
    def method(self):
    	pass
    def __hidden(self):
    	pass

obj = Classy()
print(obj.__dict__)
print(Classy.__dict__)

print(Classy.__name__)
print(type(obj).__name__)

print(Classy.__module__)

print(Classy.__bases__)













