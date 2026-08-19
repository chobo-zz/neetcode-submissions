class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}

        def dfs(i): # returns max score diff starting at stoneValue[i:]
            if i == len(stoneValue):
                return 0
            
            if i in memo:
                return memo[i]
            
            playerScore = 0
            maxScoreDiff = float("-inf")
            for j in range(i, min(len(stoneValue), i + 3)):
                playerScore += stoneValue[j]
                maxScoreDiff = max(maxScoreDiff, playerScore - dfs(j + 1))
            memo[i] = maxScoreDiff
            return maxScoreDiff
        
        res = dfs(0)
        if res == 0:
            return "Tie"
        return "Alice" if res > 0 else "Bob"