class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l, r = 0, x // 2
        res = 0

        while l <= r:
            m = (l + r) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            elif m * m <= x:
                l = m + 1
                res = m
        
        return res

        # 13
        # 4, 4
        # 5
        
