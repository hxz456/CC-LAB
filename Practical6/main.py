class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def insert(self, element):
        self.queue.append(element)
        self.queue.sort()
    
    def remove(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

def product_of_three_largest_distinct(nums):
    # Remove duplicates by converting the list to a set
    nums_set = set(nums)
    
    # Initialize a priority queue
    pq = PriorityQueue()
    
    # Add elements to the priority queue
    for num in nums_set:
        pq.insert(num)
        if len(pq.queue) > 3:
            pq.remove()
    
    # Check if there are at least three distinct elements
    if len(pq.queue) < 3:
        raise ValueError("The list must contain at least three distinct elements.")
    
    # Calculate the product of the three largest distinct elements
    product = 1
    while not pq.is_empty():
        product *= pq.remove()
    
    return product

# Example usage
nums = [10, 20, 20, 30, 50, 7, 7]
try:
    result = product_of_three_largest_distinct(nums)
    print(f"Product of the three largest distinct elements: {result}")
except ValueError as e:
    print(e)
