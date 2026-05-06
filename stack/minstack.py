class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stacl = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stacl:
            self.min_stacl.append(val)
        else:
            self.min_stacl.append(min(self.min_stacl[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stacl.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stacl[-1]