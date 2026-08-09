class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        seen = set(nums)

        res = 1
        for num in nums:
            if num - 1 in seen:
                continue
            else:
                streak = 1
                while num + streak in seen:
                    streak += 1
                    res = max(res, streak)
        return res