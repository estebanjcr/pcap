# Queue data structure
# FIFO: First-In First-Out

class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
    	self.queue = []
    	
    def put(self, elem):
    	self.queue.insert(0, elem)
    
    def get(self):
    	if len(self.queue) > 0:
    		elem = self.queue[-1]
    		del self.queue[-1]
    		return elem
    	else:
    		raise QueueError

queue_object_1 = Queue()
queue_object_1.put(3)
queue_object_1.put("string")
queue_object_1.put(True)
queue_object_1.get()
print(queue_object_1.queue)

class SuperQueue(Queue):
    def isempty(self):
    	return len(self.queue) == 0   # var must be public

queue_object_2 = SuperQueue()
print(queue_object_2.isempty())
queue_object_2.put(3)
queue_object_2.put("string")
queue_object_2.put(True)
print(len(queue_object_2.queue))
print(queue_object_2.isempty())