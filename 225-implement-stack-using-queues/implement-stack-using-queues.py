class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()        

    def top(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        res = self.q.popleft()
        self.push(res)
        return res

    def empty(self) -> bool:
        return True if not self.q else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()