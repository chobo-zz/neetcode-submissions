class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {} # value -> indices

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in mp:
                return [mp[difference], i]
            mp[nums[i]] = i
