class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMatrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        rows, cols = len(self.sumMatrix), len(self.sumMatrix[0])

        for r in range(1, rows):
            prefix = 0
            for c in range(1, cols):
                prefix += matrix[r - 1][c - 1]
                sumAbove = self.sumMatrix[r - 1][c]
                self.sumMatrix[r][c] = prefix + sumAbove

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        bottomRight = self.sumMatrix[row2][col2]
        topLeft = self.sumMatrix[row1 - 1][col1 - 1]
        left = self.sumMatrix[row2][col1 - 1]
        top = self.sumMatrix[row1 - 1][col2]

        return bottomRight - left - top + topLeft




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)