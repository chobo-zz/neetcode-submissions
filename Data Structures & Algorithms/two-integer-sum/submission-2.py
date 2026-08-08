class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # value -> index

        for index, value in enumerate(nums):
            difference = target - value
            if difference in hash_map:
                return [hash_map[difference], index]
            hash_map[value] = index