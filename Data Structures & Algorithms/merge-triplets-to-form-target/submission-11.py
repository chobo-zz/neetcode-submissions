class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            if x == target[0]:
                good.add(0)
            if y == target[1]:
                good.add(1)
            if z == target[2]:
                good.add(2)


        return len(good) == 3