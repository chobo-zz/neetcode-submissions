class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(n)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
        
        return True if slow == 1 else False
        
    def sumOfSquares(self, n):
        res = 0

        while n:
            digit = n % 10
            n = n // 10
            res += digit ** 2
        
        return res