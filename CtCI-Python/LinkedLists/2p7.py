import sys

sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from linked_list import LinkedList
from node import Node

def intersection(h1, h2):
    curr = h1
    h1_set = set()
    while curr != None:
        h1_set.add(curr)
        curr = curr.next
    curr = h2
    while curr != None:
        if curr in h1_set:
            return curr
        curr = curr.next
    return None


head = Node("A")
ll1 = LinkedList(head)
n1 = Node("B")
# n2 = Node("A")
n2 = Node("C")
n3 = Node("D")
n4 = Node("P")
n5 = Node("Q")
n6 = Node("R")
# n7 = Node("C")
# n8 = Node("C")
ll1.append_node(n1)
ll1.append_node(n2)
ll1.append_node(n3)

ll2 = LinkedList(n4)

# ll2.append_node(n4)
ll2.append_node(n5)
ll2.append_node(n6)
ll2.append_node(n1)
# ll2.append_node(n7)
# ll2.append_node(n8)
ll1.print_ll()
ll2.print_ll()
node1 = intersection(head, n4)
print(node1.data)
