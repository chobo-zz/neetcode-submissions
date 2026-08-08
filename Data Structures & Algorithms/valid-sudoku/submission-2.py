class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set for tracking row values
        # set for tracking col values
        # set for tracking square values

        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        # iterate through the entire grid, nested for loop (row -> col)
        # check if each cell value exists in all 3 sets, if does, return false, if doesnt, continue and add seen value to sets
        # return true once full iteration complete

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r // 3, c // 3)]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True