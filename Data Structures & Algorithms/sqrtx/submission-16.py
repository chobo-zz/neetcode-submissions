class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        if x <= 2:
            return 1
        l, r = 0, x // 2
        res = l
        while l <= r:
            m = (l + r) // 2
            squared = m * m
            
            if squared > x:
                r = m - 1
                
            elif squared <= x:
                l = m + 1
                res = m
                
        return res
            