class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        # returns max score difference between current player and opponent
        def dfs(i, M):
            if i >= len(piles):
                return 0
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            curSum = 0
            res = float("-inf")
            for j in range(i, min(len(piles), i + 2 * M)):
                curSum += piles[j]

                X = j - i + 1
                res = max(res, curSum - dfs(j + 1, max(M, X)))
            
            memo[(i, M)] = res
            return res
        
        total = sum(piles)
        aliceDiff = dfs(0, 1)
        # a + b + a - b = total sum + difference
        # 2a = totalsum + difference
        # a = (totalSum + difference) // 2
        return (total + aliceDiff) // 2

        
            

