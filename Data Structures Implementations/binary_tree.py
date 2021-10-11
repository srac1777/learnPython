from collections import deque
from binary_tree_node import BinaryTreeNode


j = BinaryTreeNode("J")
i = BinaryTreeNode("I")
h = BinaryTreeNode("H")
g = BinaryTreeNode("G", None, h)
f = BinaryTreeNode("F", j)
e = BinaryTreeNode("E", g ,i)
d = BinaryTreeNode("D")
c = BinaryTreeNode("C", None, f)
b = BinaryTreeNode("B", d, e)
a = BinaryTreeNode("A", b, c)

def preorder_traversal(root):
    if root == None:
        return
    print(root.data)
    preorder_traversal(root.leftChild)
    preorder_traversal(root.rightChild)
    

def inorder_traversal(root):
    if root == None:
        return
    inorder_traversal(root.leftChild)
    print(root.data)
    inorder_traversal(root.rightChild)
    

def postorder_traversal(root):
    if root == None:
        return
    postorder_traversal(root.leftChild)
    postorder_traversal(root.rightChild)
    print(root.data)
    

def bfs(root):
    q = deque([])
    print(root.data)
    q.append(root.leftChild)
    q.append(root.rightChild)
    while len(q) > 0:
        curr = q.popleft()
        print(curr.data)
        if curr.leftChild:
            q.append(curr.leftChild)
        if curr.rightChild:
            q.append(curr.rightChild)

def dfs(root):
    if root == None:
        return
    dfs(root.leftChild)
    dfs(root.rightChild)
    print(root.data)
    

dfs(a)
