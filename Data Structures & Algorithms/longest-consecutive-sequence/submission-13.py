class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        res = 1

        for num in nums:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                    res = max(res, length)
        
        return res
