class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def isLeaf(n):
    return n.left is None and n.right is None

# Collect left boundary nodes (top-down)
def leftBoundary(root, res):
    if not root or isLeaf(root):
        return
    res.append(root.data)
    if root.left:
        leftBoundary(root.left, res)
    elif root.right:
        leftBoundary(root.right, res)

# Collect leaf nodes
def leaves(root, res):
    if not root:
        return
    if isLeaf(root):
        res.append(root.data)
        return
    leaves(root.left, res)
    leaves(root.right, res)

# Collect right boundary nodes (bottom-up)
def rightBoundary(root, res):
    if not root or isLeaf(root):
        return
    if root.right:
        rightBoundary(root.right, res)
    elif root.left:
        rightBoundary(root.left, res)
    res.append(root.data)

# Main function for boundary traversal
def boundaryTraversal(root):
    res = []
    if not root:
        return res

    if not isLeaf(root):
        res.append(root.data)  # Root node (if not a leaf)

    leftBoundary(root.left, res)
    leaves(root, res)
    rightBoundary(root.right, res)

    return res

# Example with smaller data
if __name__ == "__main__":
    # Creating a small binary tree
    #      1
    #     / \
    #    2   3
    #     \
    #      4
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)

    boundary = boundaryTraversal(root)        
    print(' '.join(map(str, boundary)))
