class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        negDiag = set()
        posDiag = set()
        res = []

        board = [["."] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r - c) in negDiag or (r + c) in posDiag:
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                negDiag.add((r - c))
                posDiag.add((r + c))

                dfs(r + 1)

                board[r][c] = "."
                col.remove(c)
                negDiag.remove((r - c))
                posDiag.remove((r + c))
                

        dfs(0)
        return res