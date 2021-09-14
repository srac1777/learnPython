import sys

sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from node import Node
from linked_list import LinkedList

def remove_dups(head):
    if head.next == None:
        return head

    hsh = {}
    curr = head
    hsh[curr.data] = True
    
    while curr != None and curr.next != None:
        if curr.next.data not in hsh:
            hsh[curr.next.data] = True
            curr = curr.next
        else:
            curr.next = curr.next.next # delete the curr.next node
    
    return head

def remove_dups_no_buffer(head):
    if head.next == None:
        return head
    
    main_itr = head
    while main_itr != None and main_itr.next != None:
        curr_itr = main_itr
        while curr_itr.next != None:
            if curr_itr.next.data == main_itr.data:
                curr_itr.next = curr_itr.next.next
            else:
                curr_itr = curr_itr.next
        main_itr = main_itr.next
    return head

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
remove_dups_no_buffer(head)
ll.print_ll()

