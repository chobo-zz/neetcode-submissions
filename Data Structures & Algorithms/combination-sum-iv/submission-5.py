class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 1
            
            if remaining in memo:
                return memo[remaining]
            
            combinations = 0
            for num in nums:
                if remaining - num >= 0:
                    combinations += dfs(remaining - num)
            
            memo[remaining] = combinations
            return combinations
        
        return dfs(target)
