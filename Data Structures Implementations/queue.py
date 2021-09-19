import sys

sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from node import Node

class MyQueue:
    def __init__(self):
        self.data = None
        self.start = None
        self.end = None
    
    def add(self, val):
        if self.data == None:
            self.data = Node(val)
            self.start = self.data
            self.end = self.data
        else:
            self.end.next = Node(val)
            self.end = self.end.next
        
    def remove(self):
        if self.start == None:
            print("empty")
        else:
            to_return = self.start.data
            self.start = self.start.next
            if self.start == None:
                self.end = None
            return to_return
            
    def peek(self):
        return self.start and self.start.data
    
    def isEmpty(self):
        return self.start == None
    
q = MyQueue()
q.add(1)
q.add(3)
q.add(2)
q.add(7)
# s.print_stack()
# b = q.remove()
# s.print_stack()
# print(q.start.data)
# print(q.start.next.data)
# print(q.start.next.next.data)
# print(q.start.next.next.next.data)
a = q.remove()
print(a)
print(q.start.data)
b = q.remove()
print(b)
print(q.start.data)
q.remove()
# print(q.start.data)
# s.print_stack()
print(q.start.data)
q.remove()
# q.remove()
print(q.start)
q.remove()
