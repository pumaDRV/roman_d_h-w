class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
for item in range(10):
    stack.push(item)

while not stack.is_empty():
    print(stack.pop(), end=" ")
print()

stack = Stack()
stack.push("Hello,")
stack.push("world!")
while not stack.is_empty():
    print(stack.pop(), end=" ")