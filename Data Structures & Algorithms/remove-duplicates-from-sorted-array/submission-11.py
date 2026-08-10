class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write = 0, 0

        while read < len(nums):
            nums[write] = nums[read]
            
            while read < len(nums) and nums[read] == nums[write]:
                read += 1
            write += 1
        return write