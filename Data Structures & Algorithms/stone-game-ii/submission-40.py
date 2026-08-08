class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        # a + b = totalStones
        # a - b = stoneDiff
        # (a + b) + (a - b) = totalStones + stoneDiff
        # 2a = totalStones + stoneDiff
        # a = (totalStones + stoneDiff) // 2

        totalStones = sum(piles)

        def dfs(i, M):
            if i == len(piles):
                return 0
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            curSum = 0
            maxStoneDiff = float("-inf")
            for j in range(i, min(len(piles), i + 2 * M)):
                curSum += piles[j]
                X = j - i + 1
                maxStoneDiff = max(maxStoneDiff, curSum - dfs(j + 1, max(M, X)))

            memo[(i, M)] = maxStoneDiff
            return maxStoneDiff

        aliceStoneDiff = dfs(0, 1)
        aliceScore = (totalStones + aliceStoneDiff) // 2
        return aliceScore