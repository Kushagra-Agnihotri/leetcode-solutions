class MinStack:

    def __init__(self):
        self.stk = []
        self.min_heap = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        self.min_heap.append( min((self.min_heap[-1] if self.min_heap else 1e18), val ))
    def pop(self) -> None:
        if self.stk:
            self.stk.pop()
            self.min_heap.pop()
        

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min_heap[-1]
        
