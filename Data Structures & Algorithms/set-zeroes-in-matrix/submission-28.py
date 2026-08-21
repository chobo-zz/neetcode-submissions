class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False

        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r == 0:
                        rowZero = True
                    else:
                        matrix[r][0] = 0
        
        for r in range(1, rows):
            for c in range(1, cols):
                if not matrix[0][c] or not matrix[r][0]:
                    matrix[r][c] = 0
        
        if not matrix[0][0]:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0