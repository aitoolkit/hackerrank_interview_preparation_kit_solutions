class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def put(self, value):
        self.stack1.append(value)
