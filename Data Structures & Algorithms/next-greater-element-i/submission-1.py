class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = { val: index for index, val in enumerate(nums1) }

        stack = []
        res = [-1] * len(nums1)

        for num in nums2:
            while stack and stack[-1] < num:
                stackVal = stack.pop()
                index = indexes[stackVal]
                res[index] = num

            if num in indexes:
                stack.append(num)
        return res
