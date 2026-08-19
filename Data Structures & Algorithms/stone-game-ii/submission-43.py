class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        total = sum(piles)

        def dfs(i, M):
            if i == len(piles):
                return 0
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            curSum = 0
            maxScoreDiff = float("-inf")
            for j in range(i, min(len(piles), i + 2 * M)):
                curSum += piles[j]
                maxScoreDiff = max(maxScoreDiff, curSum - dfs(j + 1, max(M, j - i + 1)))
            
            memo[(i, M)] = maxScoreDiff
            return maxScoreDiff

        # a + b = total
        # a - b = diff
        # 2a = total + diff
        # a = (total + diff) // 2

        
        diff = dfs(0, 1)
        return (total + diff) // 2