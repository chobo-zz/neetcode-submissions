class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        grid = [["."] * n for _ in range(n)]

        col = set()
        negDiag = set()
        posDiag = set()

        def dfs(r):
            nonlocal res

            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag or grid[r][c] != ".":
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                grid[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                grid[r][c] = "."
        
        dfs(0)
        return res