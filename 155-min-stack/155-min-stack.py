class MinStack:

    def __init__(self):
        self.k=[]
        
    def push(self, val: int) -> None:
        self.val=val
        self.k.append(val) 

    def pop(self) -> None:
            self.k.pop()
        

    def top(self) -> int:
        return self.k[-1]

    def getMin(self) -> int:
        return min(self.k)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()