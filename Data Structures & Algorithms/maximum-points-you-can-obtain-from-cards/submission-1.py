class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        memo = {}

        def dfs(i, j, k): # returns max point possible with i cards left to choose
            if not i:
                return 0
            
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            takeJ = cardPoints[j] + dfs(i - 1, j + 1, k)
            takeK = cardPoints[k] + dfs(i - 1, j, k - 1)
            memo[(i, j, k)] = max(takeJ, takeK)
            
            return memo[(i, j, k)]
        
        return dfs(k, 0, len(cardPoints) - 1)
            
