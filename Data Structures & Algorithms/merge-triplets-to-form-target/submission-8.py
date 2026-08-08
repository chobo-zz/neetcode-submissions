class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set()

        for i in range(len(triplets)):
            x, y, z = triplets[i]
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            if x == target[0]:
                valid.add(0)
            if y == target[1]:
                valid.add(1)
            if z == target[2]:
                valid.add(2)
        
        return len(valid) == 3