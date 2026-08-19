class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(curSum):
            if curSum == target:
                return 1
            
            if curSum in memo:
                return memo[curSum]
            
            res = 0
            for num in nums:
                if num + curSum <= target:
                    res += dfs(curSum + num)
            memo[curSum] = res
            return res
        
        return dfs(0)