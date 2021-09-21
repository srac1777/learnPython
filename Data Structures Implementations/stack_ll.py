from node import Node

class StackLL:
    def __init__(self, val):
        self.top = Node(val)
    
    def isEmpty(self):
        return self.top == None
    
    def peek(self):
        if self.isEmpty():
            return "stack empty"
        return self.top.data
    
    def push(self,val):
        if self.isEmpty():
            self.top = Node(val)
        else:
            node = Node(val)
            node.next = self.top
            self.top = node
    
    def pop(self):
        if self.isEmpty():
            return "nothing to pop"
        to_pop = self.top
        self.top = self.top.next
        return to_pop.data

s = StackLL(4)
print(s.peek())
print(s.isEmpty())
k = s.pop()
print(k)
print(s.peek())
s.push(5)
s.push(1)
m = s.pop()
print(m)
s.push(2)
s.push(3)
print(s.peek())
s.pop()
s.pop()
p = s.pop()
print(p)
s.pop()
s.pop()
