class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack_min.append(val)
        else:
            self.stack_min.append(min(val,self.stack_min[-1]))
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack_min.pop()
        self.stack.pop()


    def top(self) -> int:
        
        return self.stack[-1]


    def getMin(self) -> int:
        return self.stack_min[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
