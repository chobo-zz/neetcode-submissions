class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(m):
            curSum = 0
            daysLeft = days
            for w in weights:
                
                if curSum + w > m:
                    daysLeft -= 1
                    curSum = 0
                    if not daysLeft:
                        return False
                curSum += w
            return True

        l, r = max(weights), sum(weights)
        minimumPossible = r
        while l <= r:
            m = (l + r) // 2
            
            if canShip(m):
                minimumPossible = m
                r = m - 1
            else:
                l = m + 1
        return minimumPossible
        
        

