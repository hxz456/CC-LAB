class MyQueue:
    def __init__(self, c):
        self.l = [None] * c
        self.cap = c  
        self.size = 0  
        self.front = 0  

    def getFront(self):
      
      
        if self.size == 0:
            return None
        return self.l[self.front]  

    def getRear(self):
      
        # Check if queue is empty
        if self.size == 0:
            return None
          
        # Calculate rear index
        rear = (self.front + self.size - 1) % self.cap  
        return self.l[rear]  

    def enqueue(self, x):
      
        # Check if queue is full
        if self.size == self.cap:
            return
          
        # Calculate rear index
        rear = (self.front + self.size) % self.cap  
        self.l[rear] = x 
        self.size += 1 

    def dequeue(self):
      
        # Check if queue is empty
        if self.size == 0:
            return None
        res = self.l[self.front]  
        
        # Move front index circularly
        self.front = (self.front + 1) % self.cap 
        self.size -= 1  
        return res  
q = MyQueue(4)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

# Call getFront and getRear after all enqueues
print(q.getFront(), q.getRear())

q.enqueue(50)  # This won't be added as the queue is full

q.dequeue()
q.dequeue()

# Call getFront and getRear after dequeues and new enqueue
print(q.getFront(), q.getRear())

q.enqueue(50)
print(q.getFront(), q.getRear())
