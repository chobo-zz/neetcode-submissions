class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        read = 0
        k = 0
        while read < len(nums):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
                k += 1
            read += 1
        return k
