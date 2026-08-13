class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity):
            curDays = 1
            curWeight = 0
            for w in weights:
                if w + curWeight > capacity:
                    curWeight = 0
                    curDays += 1
                    if curDays > days:
                        return False
                curWeight += w
            return True
        
                    

        l, r = max(weights), sum(weights)
        res = sum(weights)
        while l <= r:
            m = (l + r) // 2

            if canShip(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res