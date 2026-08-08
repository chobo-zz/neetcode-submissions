class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(row, col, index):

            if index == len(word):
                return True

            
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or 
                (row, col) in visited or word[index] != board[row][col]):
                return False
            
            visited.add((row, col))

            res = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )

            visited.remove((row, col))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False