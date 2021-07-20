class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, val: int) -> None:
        if not len(self.stack) > 0:
            self.stack.append((val, val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))


    def pop(self) -> None:
        if self.stack: self.stack.pop()[0]

    def top(self) -> int:
        if self.stack: return self.stack[-1][0]
        else: return None

    def getMin(self) -> int:
        if self.stack: return self.stack[-1][1]
        else: return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()