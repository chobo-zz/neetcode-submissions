class CountSquares:

    def __init__(self):
        self.pts = []
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for point in self.pts:
            x, y = point

            if abs(px - x) != abs(py - y) or px == x and py == y:
                continue
                
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        
        return res
