class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)

        index = 0
        for i in range(3):
            while count[i]:
                nums[index] = i
                count[i] -= 1
                index += 1
        