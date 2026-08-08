class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = 0
        k = 0
        while read < len(nums):
            if nums[read] != val:
                nums[k] = nums[read]
                k += 1
            read += 1
        return k
