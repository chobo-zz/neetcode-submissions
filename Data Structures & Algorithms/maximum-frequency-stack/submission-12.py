class FreqStack:

    def __init__(self):
        self.valToFreq = defaultdict(int)
        self.freqToStack = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.valToFreq[val] += 1
        self.maxFreq = max(self.maxFreq, self.valToFreq[val])
        self.freqToStack[self.valToFreq[val]].append(val)

    def pop(self) -> int:
        res = self.freqToStack[self.maxFreq].pop()
        self.valToFreq[res] -= 1
        if len(self.freqToStack[self.maxFreq]) == 0:
            self.maxFreq = max(0, self.maxFreq - 1)
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()