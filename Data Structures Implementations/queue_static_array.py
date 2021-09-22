class QSA:
    def __init__(self, maxSize = 4):
        self.queue = [None]*maxSize
        self.start = 0
        self.end = 0
    
    def printQ(self):
        print(self.queue)
    
    def enqueue(self, val):
        if self.isFull():
            print("queue full")
            return
        if self.start == self.end and self.queue[self.start] == None:
            self.queue[self.start] = val
            return
        self.end = (self.end + 1) % len(self.queue)
        self.queue[self.end] = val
        
    def dequeue(self):
        if self.queue[self.start] == None:
            print("q empty")
            return
        s = self.queue[self.start]
        self.queue[self.start] = None
        if self.start != self.end:
            self.start = (self.start + 1) % len(self.queue)
        return s
    
    def peek(self):
        if self.start == None:
            return "empty"
        return self.queue[self.start]
    
    def isFull(self):
        return self.start == (self.end + 1) % len(self.queue)
    

q = QSA()
q.enqueue(3)
q.printQ()
q.enqueue(5)
q.printQ()
q.enqueue(9)
q.printQ()
q.enqueue(1)
q.printQ()
print(q.start)
print(q.end)
print("========")
m = q.dequeue()
print(m)

q.printQ()
q.dequeue()
q.dequeue()
q.printQ()
print(q.start)
print(q.end)
q.dequeue()
print(q.start)
print(q.end)
q.printQ()
q.enqueue(7)
q.enqueue(2)
q.printQ()
q.dequeue()
q.printQ()
q.enqueue(5)
q.printQ()
q.dequeue()
q.printQ()
