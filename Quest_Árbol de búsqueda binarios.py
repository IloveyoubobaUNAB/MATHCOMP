
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end=" ")
        inorderTraversal(root.right)

def preorderTraversal(root):
    if root:
        print(root.data, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data, end=" ")

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return 1 + max(left_height, right_height)

def depth(root):
    if root is None:
        return 0
    else:
        return 1 + max(depth(root.left), depth(root.right))

# Crear el árbol
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

# Imprimir los recorridos
print("InOrder Traversal:", end=" ")
inorderTraversal(root)
print("\nPreOrder Traversal:", end=" ")
preorderTraversal(root)
print("\nPostOrder Traversal:", end=" ")
postorderTraversal(root)

# Imprimir la altura y la profundidad
print("\nAltura del árbol:", height(root))
print("Profundidad del árbol:", depth(root))