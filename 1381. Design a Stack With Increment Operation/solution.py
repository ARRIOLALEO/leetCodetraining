class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [] 
        self.max = maxSize

    def push(self, x: int) -> None:
        if self.stack == []:
            self.stack.append(x)
        elif len(self.stack) < self.max:
            self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack != []:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val
