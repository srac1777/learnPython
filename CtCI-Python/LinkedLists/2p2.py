import sys

sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from node import Node
from linked_list import LinkedList

def k_to_last_arr(head, k):
    arr = []
    curr = head
    while curr != None:
        arr.append(curr)
        curr = curr.next
        
    if k <= len(arr):
        return arr[-k]
    else:
        return "oops"

def k_to_last(head, k):
    main_itr = head
    while main_itr != None:
        curr_itr = main_itr
        for i in range(0,k):
            if i != k-1 and curr_itr.next == None:
                return "k-error"
            
            if curr_itr.next == None:
                return main_itr
            else:
                curr_itr = curr_itr.next
        main_itr = main_itr.next


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
node1 = k_to_last(head, 7)
print(node1.data)

                
