class CountSquares:

    def __init__(self):
        self.points = []
        self.pointCounts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        pair = (point[0], point[1])
        self.points.append(pair)
        self.pointCounts[pair] += 1
        

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for x2, y2 in self.points:
            if abs(x1 - x2) == abs(y1 - y2) and y1 != y2: # diagonal found
                res += self.pointCounts[(x1, y2)] * self.pointCounts[(x2, y1)]

        return res
