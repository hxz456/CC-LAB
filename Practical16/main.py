class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

def isMirror(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return (root1.val == root2.val) and isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)

root1 = TNode(1)
root1.left = TNode(2)
root1.right = TNode(3)

root2 = TNode(1)
root2.left = TNode(3)
root2.right = TNode(2)

print("Mirrored:" if isMirror(root1, root2) else "Not mirrored.")
