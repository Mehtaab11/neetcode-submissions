class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mini or self.mini[-1] >= val:
            self.mini.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.mini[-1]:
            self.mini.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
