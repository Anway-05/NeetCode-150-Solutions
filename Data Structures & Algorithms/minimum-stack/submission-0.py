class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
        self.stack.append(val)
        return None

    def pop(self) -> None:
        value=self.stack.pop()
        if value==self.min_stack[-1]:
            self.min_stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
