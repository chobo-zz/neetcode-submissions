class RandomizedSet:

    def __init__(self):
        self.valToIdx = defaultdict(int)
        self.val = []

    def insert(self, val: int) -> bool:
        if val in self.valToIdx:
            return False
        self.valToIdx[val] = len(self.val)
        self.val.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.valToIdx:
            return False
        lastVal = self.val[-1]
        lastIdx = self.valToIdx[lastVal]

        idx = self.valToIdx[val]

        self.val[idx] = lastVal
        self.valToIdx[lastVal] = idx
        self.val.pop()
        del self.valToIdx[val]

    def getRandom(self) -> int:
        return random.choice(self.val)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()