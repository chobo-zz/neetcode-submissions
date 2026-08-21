class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        def helper(x, n):
            if n == 0:
                return 1
            
            subres = helper(x, n // 2)
            subres = subres * subres

            if n % 2:
                subres = subres * x
            return subres

        return helper(x, n) if n > 0 else 1 / helper(x, abs(n))