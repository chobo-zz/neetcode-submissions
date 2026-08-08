class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int) # value -> index

        for i, v in enumerate(nums):
            complement = target - v
            if complement in seen:
                return [seen[complement], i]
            seen[v] = i
        