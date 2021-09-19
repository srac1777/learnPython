import sys

sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from linked_list import LinkedList
from node import Node

def loop_detection(head):
    a = set()
    curr = head
    
    while curr not in a:
        a.add(curr)
        curr = curr.next
    
    return curr


head = Node("A")
ll = LinkedList(head)
n1 = Node("B")
n2 = Node("C")
n3 = Node("D")
n4 = Node("E")
n5 = Node("F")
# n5 = Node("B")
# n6 = Node("B")
# n7 = Node("C")
# n8 = Node("C")
ll.append_node(n1)
ll.append_node(n2)
ll.append_node(n3)
ll.append_node(n4)
ll.append_node(n5)
n5.next = head
# ll.append_node(n6)
# ll.append_node(n7)
# ll.append_node(n8)
# ll.print_ll()
node1 = loop_detection(head)
print(node1.data)
