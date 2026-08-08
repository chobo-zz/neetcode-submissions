class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        # returns max score difference current player can get
        # from piles[i:] with current M = m
        def dfs(i, m): 
            if i >= len(piles):
                return 0
            
            if (i, m) in memo:
                return memo[(i, m)]

            res = float("-inf")
            curSum = 0

            for j in range(i, min(len(piles), i + 2 * m)):
                curSum += piles[j]

                x = j - i + 1  # number of piles taken
                res = max(res, curSum - dfs(j + 1, max(m, x)))
            
            memo[(i, m)] = res
            return res
        
        total = sum(piles)
        scoreDiff = dfs(0, 1)

        return (total + scoreDiff) // 2
        # a + b = total
        # a - b = diff
        # (a + b) + (a - b) = total + diff