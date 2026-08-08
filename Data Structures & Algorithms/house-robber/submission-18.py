class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} # max robbed at index i (i -> max possible)

        def dfs(i): # returns max possible money up to this index
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        
        return max(dfs(0), dfs(1))