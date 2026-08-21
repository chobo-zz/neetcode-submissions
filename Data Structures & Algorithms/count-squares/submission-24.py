class CountSquares:

    def __init__(self):
        self.pts = []
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point

        for px, py in self.pts:
            if abs(px - x) != abs(py - y) or x == px:
                continue
            res += self.ptsCount[(px, y)] * self.ptsCount[(x, py)]
        return res