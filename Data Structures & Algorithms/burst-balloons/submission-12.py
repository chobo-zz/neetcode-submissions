class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]
        
        def dfs(l, r): # returns max coins gained from popping balloons[l:r + 1]
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            maxCoins = 0
            for i in range(l, r + 1):
                coins = nums[i] * nums[l - 1] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                maxCoins = max(maxCoins, coins)
            
            memo[(l, r)] = maxCoins
            return maxCoins
        
        return dfs(1, len(nums) - 2)
        