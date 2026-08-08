class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        # returns alice's max score at any turn
        def dfs(i, M, isAliceTurn):
            if i >= len(piles):
                return 0
            
            if (i, M, isAliceTurn) in memo:
                return memo[(i, M, isAliceTurn)]
            
            res = float("-inf") if isAliceTurn else float("inf")
            curSum = 0
            for j in range(i, min(len(piles), i + M * 2)):
                X = j - i + 1
                if isAliceTurn:
                    curSum += piles[j]
                    res = max(res, curSum + dfs(j + 1, max(X, M), False))
                else:
                    res = min(res, dfs(j + 1, max(X, M), True))
            
            memo[(i, M, isAliceTurn)] = res
            return res
        
        return dfs(0, 1, True)