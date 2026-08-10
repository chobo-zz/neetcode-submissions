class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write = 1, 1

        while read < len(nums):
            if nums[read] == nums[read - 1]:
                read += 1
                continue
            nums[write] = nums[read]
            read += 1
            write += 1
            
    
        return write