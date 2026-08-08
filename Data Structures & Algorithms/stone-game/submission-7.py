class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(i, j): # returns max diff between alice and bob starting at turn i
            if i > j:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            res = float("-inf")

            if (j - i + 1) % 2 == 0:
                res = max(dfs(i + 1, j) + piles[i], dfs(i, j - 1) + piles[j])
            else:
                res = max(dfs(i + 1, j), dfs(i, j - 1))
           
            memo[(i, j)] = res
            return res
    
        total = sum(piles)
        score = dfs(0, len(piles) - 1)
        return score > total - score
            
