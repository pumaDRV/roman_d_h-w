class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
for item in range(10):
    queue.push(item)

while not queue.is_empty():
    print(queue.pop(), end=" ")
print()