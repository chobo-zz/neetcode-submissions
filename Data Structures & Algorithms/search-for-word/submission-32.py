class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visiting = set()
        
        def dfs(i, r, c):

            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visiting or board[r][c] != word[i]:
                return False

            visiting.add((r, c))
            res = (
                dfs(i + 1, r + 1, c) or
                dfs(i + 1, r - 1, c) or
                dfs(i + 1, r, c + 1) or
                dfs(i + 1, r, c - 1)
            )
            visiting.remove((r, c))

            return res
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(0, r, c):
                    return True
        
        return False
                    