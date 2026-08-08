class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
            count += (1 if candidate == nums[i] else -1)
        
        return candidate