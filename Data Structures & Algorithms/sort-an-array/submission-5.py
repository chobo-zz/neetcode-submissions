class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        minVal = min(nums)
        maxVal = max(nums)
        res = []
        
        for val in range(minVal, maxVal + 1):
            while count[val]:
                res.append(val)
                count[val] -= 1
        
        return res