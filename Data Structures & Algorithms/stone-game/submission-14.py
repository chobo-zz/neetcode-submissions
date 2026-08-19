class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(l, r): # returns max score diff
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            scoreDiffIfLeft = piles[l] - dfs(l + 1, r)
            scoreDiffIfRight = piles[r] - dfs(l, r - 1)
            memo[(l, r)] = max(scoreDiffIfLeft, scoreDiffIfRight)
            return memo[(l, r)]
        
        res = dfs(0, len(piles) - 1)
        return res > 0