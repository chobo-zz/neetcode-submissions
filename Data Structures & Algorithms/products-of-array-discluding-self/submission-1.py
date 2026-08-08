class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # keep track of prefix and postfix vars
        # prefix stores product of all numbers left of the current value
        # postfix stores product of all numbers right of the current value
        # to get the final output product for current index, multiply its prefix and postfix
        # input:  [1, 2, 4, 6]
        # prefix: [1, 1, 2, 8]
        # postfix:[48,24,6, 1]
        # output (multiply prefix/postfix values): [48, 24, 12, 8]

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
