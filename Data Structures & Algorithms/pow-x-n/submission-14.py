class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1

            res = helper(x, n // 2)
            res = res * res
            if n % 2:
                res = res * x
            return res
        
        if x == 0:
            return 0
        
        return helper(x, n) if n > 0 else (1 / helper(x, -n))
