import sys
sys.setrecursionlimit(10000)

class Node:
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i
        self.left = None
        self.right = None

def insert(root, node):
    if root == None:
        return node
    if node.x < root.x:
        root.left = insert(root.left, node)
    elif node.x > root.x:
        root.right = insert(root.right, node)
    return root
    
def preorder(node):
    if node == None:
        return []
    return [node.i] + preorder(node.left) + preorder(node.right)

def postorder(node):
    if node == None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.i]
    
def solution(nodeinfo):
    nodes = [Node(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda node: (-node.y, node.x))
    tree = nodes[0]
    for node in nodes[1:]:
        insert(tree, node)
    return [preorder(tree), postorder(tree)]