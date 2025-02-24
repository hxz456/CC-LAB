class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

# Function to insert a value in the BST
def insert(root, val):
    if not root:
        return TNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# In-order traversal of the BST (to print the tree in sorted order)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Main function to build the BST from a list of values
def build_bst(values):
    root = None
    for val in values:
        root = insert(root, val)
    return root

# Example usage
values = [7, 3, 9, 2, 5, 8, 10]
root = build_bst(values)

print("In-order traversal of the BST:")
inorder(root)  # Output will be the values sorted in ascending order
