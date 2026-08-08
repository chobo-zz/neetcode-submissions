class CountSquares:

    def __init__(self):
        self.pts = []
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts.append((point[0], point[1]))
        self.ptsCount[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for x2, y2 in self.pts:
            if abs(x1 - x2) == abs(y1 - y2) and x1 != x2:
                res += self.ptsCount[(x1, y2)] * self.ptsCount[(x2, y1)]
        return res
