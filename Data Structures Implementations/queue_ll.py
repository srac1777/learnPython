from node import Node

class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, val):
        if self.isEmpty():
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def dequeue(self):
        if self.isEmpty():
            return "nothing to dequeue"
        to_return = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return to_return

    def peek(self):
        return self.head
    def contains(self, val):
        if self.isEmpty():
            return False
        curr = self.head
        while curr != None:
            if curr.data == val:
                return True
            curr = curr.next
        return False
    def isEmpty(self):
        return self.head == None and self.tail == None

q = QueueLL()
print(q.head)
print(q.tail)
q.enqueue(3)
q.enqueue(5)
q.enqueue(9)
q.enqueue(1)
print("========")
print(q.head.data)
print(q.tail.data)
m = q.dequeue()
print(m.data)
print(q.head.data)
q.dequeue()
q.dequeue()
print(q.head.data)
print(q.tail.data)
q.dequeue()
print(q.head)
print(q.tail)
print(q.dequeue())
q.enqueue(1)
print(q.peek().data)