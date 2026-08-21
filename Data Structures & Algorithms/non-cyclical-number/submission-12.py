class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(number):
            res = 0
            while number:
                digit = number % 10
                res += digit * digit
                number = number // 10
            return res

        slow = n
        fast = sumOfSquares(n)

        while slow != fast:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
        
        return slow == 1