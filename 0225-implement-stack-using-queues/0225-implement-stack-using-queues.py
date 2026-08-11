from collections import deque
class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in  range(len(self.q)-1):
            self.q.append(self.q.popleft())
    def pop(self) -> int:
        if(not self.q):
            return "empty"
        return self.q.popleft()

    def top(self) -> int:
        if not self.q:
                return "Stack is empty"
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()