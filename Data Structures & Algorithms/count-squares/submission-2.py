class CountSquares:

    def __init__(self):
        self.ptsCount = collections.defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0

        for x, y in self.pts:
            if abs(qx - x) != abs(qy - y) or x == qx or y == qy:
                continue
            # diagonal point found

            res += self.ptsCount[(x, qy)] * self.ptsCount[(qx, y)]
        return res
        
