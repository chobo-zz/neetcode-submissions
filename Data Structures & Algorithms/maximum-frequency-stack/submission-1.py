class FreqStack:

    def __init__(self):
        self.count = defaultdict(int) # val -> freq
        self.stacks = defaultdict(list)
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.stacks[self.count[val]].append(val)
        self.maxCount = max(self.maxCount, self.count[val])

    def pop(self) -> int:
        val = self.stacks[self.maxCount].pop()
        self.count[val] -= 1
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()