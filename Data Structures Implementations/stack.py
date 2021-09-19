# Stack
# API:
#   push
#   pop
#   peek
#   isEmpty

# class Stack:
#     def __init__(self, inital=None):
#         self.data = inital or []
    
#     def push(self, val):
#         self.data.append(val)
#         return self.data
#     def pop(self):
#         if len(self.data) == 0:
#             raise ValueError("stack is empty")
#         to_return = self.data[-1]
#         self.data = self.data[:-1]
#         print(self.data)
#         return to_return

class MyStack:
    def __init__(self):
        self.data = []
        self.top = None
    
    def push(self, val):
        self.data.append(val)
        self.top = self.data[-1]
    
    def pop(self):
        if len(self.data) == 0:
            print("nothing to pop")
        else:
            to_return = self.top
            self.data = self.data[0:-1]
            if self.isEmpty():
                self.top = None
            else:
                self.top = self.data[-1]
            return to_return
    
    def peek(self):
        return self.top
    
    def isEmpty(self):
        print("b")
        return len(self.data) == 0
    
    def print_stack(self):
        print(self.data)
        
    

s = MyStack()
print(s.push(1))
print(s.push(1))
print(s.push(2))
print(s.push(7))
s.print_stack()
q = s.pop()
s.print_stack()
print(q)
s.pop()
s.pop()
s.print_stack()
s.pop()
s.pop()
s.pop()
