class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            isAliceTurn = (r - l + 1) % 2 == 0

            if isAliceTurn:
                takeLeft = piles[l] + dfs(l + 1, r)
                takeRight = piles[r] + dfs(l, r - 1)
                memo[(l, r)] = max(takeLeft, takeRight)
            else:
                takeLeft = -piles[l] + dfs(l + 1, r)
                takeRight = -piles[r] + dfs(l, r - 1)
                memo[(l, r)] = min(takeLeft, takeRight)

            return memo[(l, r)]
        
        return dfs(0, len(piles) - 1) > 0