class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
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
            