class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while True:
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l + 1, r + 1]
            elif cur < target:
                l += 1
            else:
                r -= 1
            