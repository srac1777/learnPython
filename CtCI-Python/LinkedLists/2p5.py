import sys

sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from node import Node
from linked_list import LinkedList

def sum_lists(h1, h2):
    carry = 0
    head = None
    p1 = h1
    p2 = h2
    curr_node = None
    while p1 != None or p2 != None:
        if p1 == None or p2 == None:
            break
        total = p1.data + p2.data + carry
        node_val = total % 10
        carry = int(total / 10)
        
        if head == None:
            head = Node(node_val)
            head.next = None
            curr_node = head
        else:
            curr_node.next = Node(node_val)
            curr_node = curr_node.next
        p1 = p1.next
        p2 = p2.next
    
    if p1 == None:
        while p2 != None:
            node_val = (p2.data + carry) % 10
            carry = int((p2.data + carry) / 10)
            p2 = p2.next
            curr_node.next = Node(node_val)
            curr_node = curr_node.next
    if p2 == None:
        while p1 != None:
            node_val = (p1.data + carry) % 10
            carry = int((p1.data + carry) / 10)
            p1 = p1.next
            curr_node.next = Node(node_val)
            curr_node = curr_node.next
    return head


head = Node(5)
n1 = Node(9)
n2 = Node(2)
head.next = n1
n1.next = n2
# ll1 = LinkedList(head)
n3 = Node(5)
# n4 = Node(9)
# n5 = Node(2)
# n3.next = n4
# n4.next = n5
# ll2 = LinkedList(n3)
# ll1.append_node(n1)
# ll1.append_node(n2)
# ll2.append_node(n3)
# ll2.append_node(n4)
# ll2.append_node(n5)
# ll1.print_ll()
# ll2.print_ll()
node1 = sum_lists(head, n3)
print(node1.data)
print(node1.next.data)
print(node1.next.next.data)
