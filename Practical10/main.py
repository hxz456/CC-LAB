class TNode:
    def __init__(self, v=0, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r

def isBST(root):
    def validate(n, low=-float('inf'), high=float('inf')):
        if not n:
            return True
        if not (low < n.val < high):
            return False
        return validate(n.left, low, n.val) and validate(n.right, n.val, high)
    
    return validate(root)

# Example usage
r = TNode(2)
r.left = TNode(1)
r.right = TNode(3)

print(isBST(r))  # Output: True
