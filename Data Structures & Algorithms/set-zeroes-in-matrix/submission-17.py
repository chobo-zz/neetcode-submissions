class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # in-place solution:
        # change first row values to be indicators of whether that column needs to be zeroed out
        # change first col values to be indicators of whether that row needs to be zeroed out
        # complication: matrix[0][0] can't share the same indicator (first row and col overlap eachother)
        # so we create an extra variable rowZero to be indicator of whether the first row needs to be zeroed out

        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # indicates this column needs to be zeroed out
                    matrix[0][c] = 0

                    # indicates this row needs to be zeroed out
                    # but check if its first row to avoid complication above
                    if r == 0:
                        rowZero = True
                    else:
                        matrix[r][0] = 0
        
        # zero out all columns not including first column and first row (to workaround complication)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # zero out first col
        if not matrix[0][0]:
            for r in range(rows):
                matrix[r][0] = 0 
                
        # zero out first row
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0