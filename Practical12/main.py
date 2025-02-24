class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

# Function to calculate the max depth (or depth of the tree)
def maxDepth(root):
    if not root:
        return 0  # Base case: if the node is None, depth is 0
    else:
        # Recursively find the depth of left and right subtrees, and add 1 for the current node
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

# Example usage
root = TNode(1)
root.left = TNode(2)
root.right = TNode(3)
root.left.left = TNode(4)
root.left.right = TNode(5)
root.left.left.left = TNode(6)

print("Max Depth of the Tree:", maxDepth(root))  # Output: 4
