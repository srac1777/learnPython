from node import Node

class LinkedList:
    def __init__(self, head_node):
        self.head = head_node
        
    def append_node(self, node):
        curr_node = self.head
        
        while curr_node.get_next() != None:
            curr_node = curr_node.get_next()
        
        curr_node.set_next(node)
    
    def delete_node(self, val):
        curr_node = self.head
        if self.head.get_val() == val:
            self.head = self.head.get_next()
        
        while curr_node.get_next() != None:
            if curr_node.get_next().get_val() == val:
                curr_node.set_next(curr_node.get_next().get_next())
                return # IMPORTANT
            curr_node = curr_node.get_next()
            
    def print_ll(self):
        data = []
        curr = self.head
        while curr.get_next() != None:
            data.append(curr.get_val())
            curr = curr.get_next()
        data.append(curr.get_val())
        print(data)

head = Node(5)
n1 = Node(3)
n2 = Node(4)
n3 = Node(8)
n4 = Node(9)

ll = LinkedList(head)
ll.append_node(n1)
ll.append_node(n2)
ll.append_node(n3)
ll.append_node(n4)
ll.print_ll()
ll.delete_node(4)
ll.print_ll()
ll.delete_node(5)
ll.print_ll()
ll.delete_node(9)
ll.print_ll()
