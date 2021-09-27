import sys
from collections import deque
sys.path.append(
    "/Users/shashankracherla/code/learnPython/Data Structures Implementations/")

from graph_node import GraphNode

def bfs(node, val):
    q = deque([])
    q.append(node)
    node.visited = True
    curr = node
    while len(q) > 0:
        for child in curr.children:
            if child.visited:
                continue
            else:
                if child.data == val:
                    return child
                child.visited = True
                q.append(child)
        a = q.popleft()
        print(a.data)
        # print(q)
        if(len(q)):
            curr = q[0]
    return None


# s = GraphNode("S", [])
q = GraphNode("Q", [])
# e = GraphNode("E", [q])
r = GraphNode("R", [])
# p = GraphNode("P", [])
m = GraphNode("M", [])
d = GraphNode("D", [])
c = GraphNode("C", [])
b = GraphNode("B", [])
a = GraphNode("A", [])

a.set_children([b,c])
b.set_children([a,d])
c.set_children([a,d,m,q])
d.set_children([b,c,q,m])
q.set_children([c,d,r])
m.set_children([d,c])
r.set_children([q])


node = bfs(a, "T")
print(node)