class MinStack:

    def __init__(self):
         self.q = []

    def push(self, val: int) -> None:
        curMin = self.getMin()
        if curMin == None or val < curMin:
             curMin = val
        self.q.append((val, curMin));


    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    def getMin(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()