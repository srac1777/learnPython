import sys

sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from node import Node
from linked_list import LinkedList


def delete_middle_node(node):
    if node == None or node.next == None:
        print("oops")
        return
    node.data = node.next.data
    node.next = node.next.next
    return node        


head = Node("A")
ll = LinkedList(head)
n1 = Node("B")
n2 = Node("Q")
n3 = Node("A")
n4 = Node("B")
n5 = Node("B")
n6 = Node("B")
n7 = Node("C")
n8 = Node("C")
ll.append_node(n1)
ll.append_node(n2)
ll.append_node(n3)
ll.append_node(n4)
ll.append_node(n5)
ll.append_node(n6)
ll.append_node(n7)
ll.append_node(n8)
ll.print_ll()
node1 = delete_middle_node(n2)
ll.print_ll()
