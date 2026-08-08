class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):

        memo = {} # what the max possible rob amount is starting from index i

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        
        return dfs(0)
