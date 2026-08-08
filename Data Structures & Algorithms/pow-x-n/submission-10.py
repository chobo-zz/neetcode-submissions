class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            
            subRes = helper(x, n // 2)
            subRes = subRes * subRes
            if n % 2 == 1:
                subRes *= x
            return subRes
                
        
        if x == 0:
            return 0
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res