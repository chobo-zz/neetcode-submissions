class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        first = 0
        second = 1
        third = 1

        for i in range(3, n + 1):
            fourth = first + second + third
            first = second
            second = third
            third = fourth
        return third