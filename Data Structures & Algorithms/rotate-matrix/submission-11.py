class Solution:
    # for 90 degree clockwise rotation: reverse then transpose
    # for 90 degree counter-clockwise rotation: transpose then reverse
    def rotate(self, matrix: List[List[int]]) -> None:
        a, b = 0, len(matrix) - 1

        while a < b:
            matrix[a], matrix[b] = matrix[b], matrix[a]
            a += 1
            b -= 1

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            