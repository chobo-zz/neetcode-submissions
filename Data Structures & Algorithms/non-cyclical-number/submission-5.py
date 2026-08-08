class Solution:
    def isHappy(self, n: int) -> bool:
        # floyd's algo to detect cycle (fast and slow pointers)

        slow = n
        fast = self.sumOfSquares(n)
        
        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
        return True if fast == 1 else False


    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n % 10 # get last digit from n
            output += digit ** 2
            n = n // 10 # remove last digit from n
        
        return output