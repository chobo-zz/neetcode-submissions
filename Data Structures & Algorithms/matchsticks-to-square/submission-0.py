class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLength = sum(matchsticks)

        if totalLength % 4 != 0:
            return False
        
        sideLength = totalLength // 4
        sides = [0] * 4

        matchsticks.sort(reverse=True)

        def dfs(i):
            if i >= len(matchsticks):
                return True
            
            for side in range(4):
                if matchsticks[i] + sides[side] <= sideLength:
                    sides[side] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[side] -= matchsticks[i]
            
                if sides[side] == 0:
                    break
        
            return False
        
        return dfs(0)