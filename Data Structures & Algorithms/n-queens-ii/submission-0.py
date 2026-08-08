class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()
        res = 0

        def dfs(r):
            nonlocal res

            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add((r + c))
                negDiag.add((r - c))

                dfs(r + 1)

                col.remove(c)
                posDiag.remove((r + c))
                negDiag.remove((r - c))
        
        dfs(0)
        return res
