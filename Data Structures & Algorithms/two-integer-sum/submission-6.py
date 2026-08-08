class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in mp:
                return [mp[difference], index]
            mp[value] = index