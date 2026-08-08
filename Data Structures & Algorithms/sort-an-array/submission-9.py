class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        minVal = min(nums)
        maxVal = max(nums)
        res = []
        for i in range(minVal, maxVal + 1):
            while count[i]:
                res.append(i)
                count[i] -= 1
        return res
