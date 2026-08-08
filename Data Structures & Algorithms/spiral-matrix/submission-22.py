class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bot = 0, len(matrix)
        res = []

        while left < right and top < bot:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bot):
                res.append(matrix[i][right - 1])
            right -= 1

            if left == right or top == bot:
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bot - 1][i])
            bot -= 1

            for i in range(bot - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
            