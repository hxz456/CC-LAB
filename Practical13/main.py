class Node:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


root = Node(1)
root.left, root.right = Node(2), Node(3)
root.left.left, root.left.right = Node(4), Node(5)
root.right.left, root.right.right = Node(6), Node(7)

print("Preorder:")
preorder(root)
print("\nInorder:")
inorder(root)
print("\nPostorder:")
postorder(root)
