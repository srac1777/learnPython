# Stack - data structure to ensure only uniques exist
# API:
#   push
#   pop

class Stack():
    def __init__(self, inital=None):
        self.data = inital or []
    
    def push(self, val):
        self.data.append(val)
        return self.data
    def pop(self):
        if len(self.data) == 0:
            raise ValueError("stack is empty")
        to_return = self.data[-1]
        self.data = self.data[:-1]
        print(self.data)
        return to_return

s = Stack()
print(s.push(1))
print(s.push(1))
print(s.push(2))
print(s.push(7))
q = s.pop()
print(q)
s.pop()
s.pop()
s.pop()
s.pop()
