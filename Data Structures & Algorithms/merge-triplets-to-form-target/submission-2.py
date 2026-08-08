class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        validIndexes = set()

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            for i, v in enumerate(triplet):
                if v == target[i]:
                    validIndexes.add(i)
        
        return len(validIndexes) == 3