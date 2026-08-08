class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = count = 0

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            count += (1 if candidate == nums[i] else -1)
        
        return candidate