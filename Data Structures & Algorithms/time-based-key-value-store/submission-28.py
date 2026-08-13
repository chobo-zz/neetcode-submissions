class TimeMap:

    def __init__(self):
        self.data = defaultdict(list) # key -> (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        pairs = self.data[key]  
        res = ""
        l, r = 0, len(pairs) - 1

        while l <= r:
            m = (l + r) // 2

            if pairs[m][1] <= timestamp:
                res = pairs[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

        
