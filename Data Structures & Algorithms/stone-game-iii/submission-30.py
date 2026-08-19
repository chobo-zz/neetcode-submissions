class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}

        def dfs(i): # returns max score diff starting at stones[i:]
            if i == len(stoneValue):
                return 0
            
            if i in memo:
                return memo[i]
            
            maxScoreDiff = float("-inf")
            currentPlayerScore = 0
            for j in range(i, min(len(stoneValue), i + 3)):
                currentPlayerScore += stoneValue[j]
                maxScoreDiff = max(maxScoreDiff, currentPlayerScore - dfs(j + 1))
            
            memo[i] = maxScoreDiff
            return maxScoreDiff
        
        res = dfs(0)
        if res == 0:
            return "Tie"
        elif res > 0:
            return "Alice"
        else:
            return "Bob"
