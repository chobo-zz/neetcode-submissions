class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            if nums[i] == 0:
                return 1e6

            res = 1e6
            end = i + nums[i] + 1
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            memo[i] = res
            return res
        
        return dfs(0)
                
    