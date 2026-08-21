class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        MAX = 2 ** 31 - 1
        MIN = -2 ** 31

        while x != 0:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            res = res * 10 + digit
        
        return res