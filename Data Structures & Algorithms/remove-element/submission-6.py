class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = write = 0

        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
            read += 1
        
        return write