# Python program to get intersection point of two linked list
# using count of nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to get the count of nodes in a linked list 
def getCount(head):
    cnt = 0
    curr = head
    while curr:
        cnt += 1
        curr = curr.next
    return cnt

# Function to get the intersection point of two
# linked lists where head1 has d more nodes than head2
def getIntersectionByDiff(diff, head1, head2):
    curr1 = head1
    curr2 = head2

    # Move the pointer forward by d nodes
    for _ in range(diff):
        if not curr1:
            return None
        curr1 = curr1.next

    # Move both pointers until they intersect
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next

    return None

# Function to get the intersection point of two linked lists
def intersectPoint(head1, head2):
  
    # Count the number of nodes in both linked lists
    len1 = getCount(head1)
    len2 = getCount(head2)

    diff = 0

    # If the first list is longer
    if len1 > len2:
        diff = len1 - len2
        return getIntersectionByDiff(diff, head1, head2)
    else:
        diff = len2 - len1
        return getIntersectionByDiff(diff, head2, head1)
      
if __name__ == "__main__":
  
    # creation of first list: 10 -> 15 -> 30
    head1 = Node(1)
    head1.next = Node(7)
    head1.next.next = Node(30)

    # creation of second list: 3 -> 6 -> 9 -> 15 -> 30
    head2 = Node(3)
    head2.next = Node(6)
    head2.next.next = Node(9)

    # 15 is the intersection point
    head2.next.next.next = head1.next

    intersectionPoint = intersectPoint(head1, head2)

    if not intersectionPoint:
        print("-1")
    else:
        print(intersectionPoint.data)
