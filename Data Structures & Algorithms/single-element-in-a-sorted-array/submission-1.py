class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if ((i and nums[i] == nums[i - 1]) or
                (i < n - 1 and nums[i] == nums[i + 1])
            ):
                continue
            return nums[i]