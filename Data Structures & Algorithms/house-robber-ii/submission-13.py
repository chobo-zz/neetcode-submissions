class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        memo = {} # max we can rob starting from i (i -> max possible)

        def dfs(i): # returns max possible starting from i
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]

        return dfs(0)
        