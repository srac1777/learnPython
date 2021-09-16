import sys

sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from linked_list import LinkedList
from node import Node

def palindrome(head):
    arr = []
    curr = head
    
    while curr != None:
        arr.append(curr.data)
        curr = curr.next
    return check_palindrome(arr)

def check_palindrome(arr):
    n = len(arr)
    for i in range(int(n/2)):
        if arr[i] != arr[-i-1]:
            return False
    return True


head = Node("A")
ll = LinkedList(head)
n1 = Node("B")
n2 = Node("A")
n3 = Node("C")
# n4 = Node("A")
# n4 = Node("B")
# n5 = Node("B")
# n6 = Node("B")
# n7 = Node("C")
# n8 = Node("C")
ll.append_node(n1)
ll.append_node(n2)
ll.append_node(n3)
# ll.append_node(n4)
# ll.append_node(n5)
# ll.append_node(n6)
# ll.append_node(n7)
# ll.append_node(n8)
ll.print_ll()
node1 = palindrome(head)
print(node1)
