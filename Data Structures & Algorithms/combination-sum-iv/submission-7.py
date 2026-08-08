class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = { 0: 1 }

        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]
            
            combinations = 0
            for num in nums:
                if remaining - num < 0:
                    break
                combinations += dfs(remaining - num)
            
            memo[remaining] = combinations
            return combinations
        
        return dfs(target)
            
