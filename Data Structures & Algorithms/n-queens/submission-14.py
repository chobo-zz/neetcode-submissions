class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()
        res = []

        def dfs(r):
            if r >= n:
                res.append(["".join(r) for r in board])
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag or board[r][c] == "Q":
                    continue
                
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                dfs(r + 1)

                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        dfs(0)
        return res