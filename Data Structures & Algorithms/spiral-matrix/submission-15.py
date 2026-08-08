class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bot = len(matrix)
        res = []

        while left < right and top < bot:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bot):
                res.append(matrix[i][right - 1])
            right -= 1

            if top >= bot or left >= right:
                return res
            
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bot - 1][i])
            bot -= 1
            
            for i in range(bot - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res