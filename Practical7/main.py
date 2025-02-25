class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to merge two sorted linked lists
def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Append any remaining nodes from either list
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next

# Create linked list for List 1: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# Create linked list for List 2: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# Print original linked lists
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

print("Original List 1:")
print_linked_list(l1)

print("Original List 2:")
print_linked_list(l2)

# Merge the two linked lists
merged_list = mergeTwoLists(l1, l2)

# Print the merged linked list
print("Merged List:")
print_linked_list(merged_list)
