class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        res = []

        while left < right and top < bottom:
            # get top row values
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get right col values
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # handles edge case where matrix only has 1 col or 1 row
            if top >= bottom or left >= right:
                break
            
            # get bot row values
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get left col values
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
            