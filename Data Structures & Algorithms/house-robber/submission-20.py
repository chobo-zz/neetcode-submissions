class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} # stores what is the max amount we can rob starting from this index (i -> max amt)
        if not nums:
            return 0

        def dfs(i): # returns what is the max we can rob til the end starting from index i
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
                
        return dfs(0)
