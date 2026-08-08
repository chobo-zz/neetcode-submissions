class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        # returns max score diff between alice and bob
        def dfs(i, M, isAliceTurn):
            if i >= len(piles):
                return 0
            
            if (i, M, isAliceTurn) in memo:
                return memo[(i, M, isAliceTurn)]
            
            res = float("-inf") if isAliceTurn else float("inf")
            curSum = 0
            for j in range(i, min(len(piles), i + M * 2)):
                X = j - i + 1
                curSum += piles[j]
                if isAliceTurn:
                    res = max(res, curSum + dfs(j + 1, max(X, M), False))
                else:
                    res = min(res, -curSum + dfs(j + 1, max(X, M), True))
            
            memo[(i, M, isAliceTurn)] = res
            return res
        
        total = sum(piles)
        aliceDiff = dfs(0, 1, True)
        # a + b + a - b = total sum + difference
        # 2a = totalsum + difference
        # a = (totalSum + difference) // 2
        return (total + aliceDiff) // 2