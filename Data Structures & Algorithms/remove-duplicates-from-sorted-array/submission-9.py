class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write = 0, 0

        while read < len(nums):
            nums[write] = nums[read]
            write += 1
            read += 1
            while read < len(nums) and nums[read] == nums[read - 1]:
                read += 1
        return write