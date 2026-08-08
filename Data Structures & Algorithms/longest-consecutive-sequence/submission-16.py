class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        LCS = 0
        for num in nums:
            if num - 1 in seen:
                continue
            else:
                streak = 1
                while (num + streak) in seen:
                     streak += 1
                LCS = max(LCS, streak)
        return LCS
                     
            