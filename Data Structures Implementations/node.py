class Node:
  def __init__(self, data, next_node=None):
    self.data = data
    self.next = next_node
    
  def get_val(self):
    return self.data
  
  def set_val(self, val):
    self.data = val
    return self.data
  
  def get_next(self):
    return self.next
  
  def set_next(self, node):
    self.next = node
    
n1 = Node(3)
n2 = Node(4,n1)
n3 = Node(5,n2)
n4 = Node(6)

print(n3.get_val())
print(n2.get_next().get_val())
n3.set_next(n4)
print(n3.get_next().get_val())