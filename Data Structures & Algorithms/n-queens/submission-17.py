class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."] * n for _ in range(n)]
        res = []

        col = set()
        posDiag = set()
        negDiag = set()
        
        def dfs(r):
            if r == n:
                res.append(["".join(r) for r in grid])
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