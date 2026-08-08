class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]
        

        def dfs(l, r):
            res = 0
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]

            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                res = max(res, coins)
            memo[(l, r)] = res
            return res
        
        return dfs(1, len(nums) - 2)